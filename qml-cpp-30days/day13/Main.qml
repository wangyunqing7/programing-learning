import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 860
    height: 580
    visible: true
    title: "Day 13 - Model + Delegate"

    SplitView {
        anchors.fill: parent

        ListView {
            id: list
            SplitView.preferredWidth: 360
            model: taskModel
            clip: true
            delegate: ItemDelegate {
                width: list.width
                text: title
                highlighted: ListView.isCurrentItem
                onClicked: list.currentIndex = index
            }
        }

        Frame {
            SplitView.fillWidth: true
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                Label { text: list.currentIndex >= 0 ? taskModel.get ? "选择了任务" : "当前任务" : "请选择任务"; font.pixelSize: 22 }
                Label { text: "点击左侧列表项，后续 App 会在这里展示详情页。"; wrapMode: Text.WordWrap }
                Button { text: "删除当前行"; enabled: list.currentIndex >= 0; onClicked: taskModel.removeTask(list.currentIndex) }
            }
        }
    }
}
