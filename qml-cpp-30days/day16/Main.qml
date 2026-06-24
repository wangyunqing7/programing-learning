import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 1040
    height: 680
    visible: true
    title: "Day 16 - App Shell"

    header: ToolBar {
        Label {
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 12
            text: "任务 / 笔记管理"
            font.bold: true
            font.pixelSize: 18
        }
    }

    SplitView {
        anchors.fill: parent
        Frame {
            SplitView.preferredWidth: 280
            ColumnLayout {
                anchors.fill: parent
                Label { text: "导航"; font.bold: true }
                Button { Layout.fillWidth: true; text: "全部任务" }
                Button { Layout.fillWidth: true; text: "笔记" }
                Button { Layout.fillWidth: true; text: "设置" }
            }
        }
        Frame {
            SplitView.fillWidth: true
            ColumnLayout {
                anchors.centerIn: parent
                Label { text: "详情区"; font.pixelSize: 28; font.bold: true }
                Label { text: "后续每天会在这个框架中加入数据模型和功能。" }
            }
        }
    }
}
