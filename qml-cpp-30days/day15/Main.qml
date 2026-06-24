import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 860
    height: 600
    visible: true
    title: "Day 15 - Mini Task App"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 12

        Label { text: "小综合：本地任务列表"; font.pixelSize: 24; font.bold: true }

        RowLayout {
            Layout.fillWidth: true
            TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "任务标题" }
            Button { text: "添加"; onClicked: { taskStore.addTask(titleInput.text); titleInput.clear() } }
        }

        ListView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: taskStore.tasks
            spacing: 8
            delegate: ItemDelegate {
                width: ListView.view.width
                text: (modelData.done ? "✓ " : "□ ") + modelData.title
                onClicked: taskStore.toggleTask(index)
                Button {
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                    text: "删除"
                    onClicked: taskStore.removeTask(index)
                }
            }
        }
    }
}
