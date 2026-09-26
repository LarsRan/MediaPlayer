import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    width: 1200
    height: 760
    visible: true
    title: "MediaPlayer"
    color: themeColors.background

    Shortcut {
        sequence: shortcuts.open_command_palette
        onActivated: backend.executeCommand("toggle_command_palette")
    }
    Shortcut {
        sequence: shortcuts.cancel
        onActivated: backend.executeCommand("cancel")
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 12

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 360
            radius: 10
            color: themeColors.surface
            border.color: themeColors.muted

            ShaderEffect {
                anchors.fill: parent
                property real t: Date.now() / 1000.0
                property color accent: themeColors.accent
                fragmentShader: "
                    varying highp vec2 qt_TexCoord0;
                    uniform highp float qt_Opacity;
                    uniform highp float t;
                    uniform lowp vec4 accent;
                    void main() {
                        highp float x = qt_TexCoord0.x;
                        highp float y = qt_TexCoord0.y;
                        highp float meter = 0.5 + 0.4 * sin(16.0 * x + t * 1.7);
                        highp float tick = smoothstep(meter - 0.015, meter + 0.015, y);
                        lowp vec3 bg = vec3(0.97, 0.97, 0.97);
                        lowp vec3 fg = mix(bg, accent.rgb, tick);
                        gl_FragColor = vec4(fg, 1.0) * qt_Opacity;
                    }
                "
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            radius: 10
            color: themeColors.surface
            border.color: themeColors.muted
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 8
                Label {
                    text: "状态"
                    font.pixelSize: 16
                    color: themeColors.text
                }
                Label {
                    text: backend.status
                    color: themeColors.text
                }
                Label {
                    text: "按 Ctrl+P 打开命令面板"
                    color: themeColors.muted
                }
            }
        }
    }

    CommandPalette {
        id: commandPalette
        parent: Overlay.overlay
        visible: backend.commandPaletteVisible
        onVisibleChanged: {
            if (visible) {
                open()
            } else {
                close()
            }
        }
        onClosed: backend.executeCommand("cancel")
    }
}
