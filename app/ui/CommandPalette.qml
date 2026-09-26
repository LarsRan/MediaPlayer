import QtQuick
import QtQuick.Controls

Popup {
    id: panel
    modal: true
    focus: true
    anchors.centerIn: parent
    width: 460
    height: 300
    background: Rectangle {
        color: themeColors.surface
        border.color: themeColors.muted
        radius: 8
    }

    Column {
        anchors.fill: parent
        anchors.margins: 16
        spacing: 10

        Label {
            text: "命令面板"
            font.pixelSize: 18
            color: themeColors.text
        }

        TextField {
            id: commandInput
            focus: true
            placeholderText: "输入命令，比如 play.pause / visualizer.industrial_meter"
            onAccepted: {
                backend.executeCommand(text)
                text = ""
                panel.close()
            }
        }

        Label {
            text: "Esc 关闭；Enter 执行"
            color: themeColors.muted
        }
    }
}
