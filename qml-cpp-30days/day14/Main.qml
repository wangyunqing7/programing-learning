import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 820
    height: 560
    visible: true
    title: "Day 14 - JSON Store"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 12

        RowLayout {
            Layout.fillWidth: true
            TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "输入一条本地数据" }
            Button { text: "添加并保存"; onClicked: { store.addItem(titleInput.text); titleInput.clear() } }
            Button { text: "重新加载"; onClicked: store.load() }
        }

        ListView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: store.items
            delegate: ItemDelegate {
                width: ListView.view.width
                text: modelData.title
            }
        }
    }
}
