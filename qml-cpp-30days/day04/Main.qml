import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 520
    visible: true
    title: "Day 04 - Controls"

    header: ToolBar {
        Label {
            anchors.centerIn: parent
            text: "Qt Quick Controls 表单"
            font.bold: true
        }
    }

    ColumnLayout {
        anchors.centerIn: parent
        width: 420
        spacing: 14

        TextField {
            id: nameField
            Layout.fillWidth: true
            placeholderText: "输入你的名字"
        }

        Slider {
            id: progress
            Layout.fillWidth: true
            from: 0
            to: 100
            value: 30
        }

        Switch {
            id: dailySwitch
            text: "今天已经学习 QML"
            checked: true
        }

        Button {
            Layout.fillWidth: true
            text: "生成学习摘要"
            onClicked: result.text = (nameField.text || "学习者")
                + "，当前进度 " + Math.round(progress.value)
                + "%，今日状态：" + (dailySwitch.checked ? "已学习" : "未学习")
        }

        Label {
            id: result
            Layout.fillWidth: true
            wrapMode: Text.WordWrap
            text: "等待输入..."
        }
    }
}
