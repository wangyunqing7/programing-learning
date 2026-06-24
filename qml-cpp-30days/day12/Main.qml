import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 820
    height: 560
    visible: true
    title: "Day 12 - QAbstractListModel"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 12

        RowLayout {
            Layout.fillWidth: true
            TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "新任务标题" }
            Button { text: "添加"; onClicked: { taskModel.addTask(titleInput.text); titleInput.clear() } }
        }

        ListView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: taskModel
            spacing: 8
            delegate: ItemDelegate {
                width: ListView.view.width
                text: (done ? "✓ " : "□ ") + title
                onClicked: taskModel.toggleDone(index)
            }
        }
    }
}
