import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    width: 1040
    height: 680
    visible: true
    title: "第 21 天 - 完整 App：完成状态"

    Component.onCompleted: {

    }

    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            Label {
                Layout.leftMargin: 12
                text: "任务 / 笔记管理"
                font.bold: true
                font.pixelSize: 18
            }
            Item { Layout.fillWidth: true }
            Label {
                Layout.rightMargin: 12
                text: "Day 21"
                color: "#475569"
            }
        }
    }

    SplitView {
        anchors.fill: parent
        orientation: Qt.Horizontal

        Frame {
            SplitView.preferredWidth: 340
            SplitView.minimumWidth: 280
            ColumnLayout {
                anchors.fill: parent
                spacing: 10

                Label {
                    text: "任务列表"
                    font.bold: true
                    font.pixelSize: 16
                }



                ListView {
                    id: taskList
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    clip: true
                    model: taskModel
                    delegate: ItemDelegate {
                        width: taskList.width
                        text: (done ? "✓ " : "□ ") + title
                        highlighted: ListView.isCurrentItem
                        onClicked: {
                            taskList.currentIndex = index
                            const item = taskModel.get(index)
                            titleField.text = item.title || ""
                            noteField.text = item.note || ""
                            categoryField.text = item.category || "默认"
                        }
                    }
                }


            }
        }

        Frame {
            SplitView.fillWidth: true
            ColumnLayout {
                anchors.fill: parent
                spacing: 12

                Label {
                    text: "详情"
                    font.bold: true
                    font.pixelSize: 16
                }

                TextField {
                    id: titleField
                    Layout.fillWidth: true
                    placeholderText: "选择左侧任务后显示标题"
                    readOnly: false
                }

                TextArea {
                    id: noteField
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    placeholderText: "任务说明或笔记"
                    readOnly: false
                    wrapMode: TextArea.Wrap
                }

                TextField {
                    id: categoryField
                    Layout.fillWidth: true
                    placeholderText: "分类"
                    text: "默认"
                    visible: false
                    readOnly: false
                }

                RowLayout {
                    Layout.fillWidth: true

                Button {
                    text: "切换完成"
                    enabled: taskList.currentIndex >= 0
                    onClicked: taskModel.toggleDone(taskList.currentIndex)
                }


                Button {
                    text: "保存修改"
                    enabled: taskList.currentIndex >= 0 && titleField.text.trim().length > 0
                    onClicked: taskModel.updateTask(taskList.currentIndex, titleField.text, noteField.text, categoryField.text)
                }


                Button {
                    text: "删除"
                    enabled: taskList.currentIndex >= 0
                    onClicked: {
                        taskModel.removeTask(taskList.currentIndex)
                        taskList.currentIndex = -1
                        titleField.text = ""
                        noteField.text = ""
                    }
                }



                    Item { Layout.fillWidth: true }
                }


            Frame {
                Layout.fillWidth: true
                ColumnLayout {
                    anchors.fill: parent
                    spacing: 8
                    Label { text: "新增任务"; font.bold: true }
                    TextField {
                        id: newTitle
                        Layout.fillWidth: true
                        placeholderText: "任务标题"
                    }
                    TextArea {
                        id: newNote
                        Layout.fillWidth: true
                        implicitHeight: 72
                        placeholderText: "简短笔记"
                    }
                    TextField {
                        id: newCategory
                        Layout.fillWidth: true
                        placeholderText: "分类，例如：学习"
                        text: "学习"
                        visible: false
                    }
                    Button {
                        text: "添加"
                        enabled: newTitle.text.trim().length > 0
                        onClicked: {
                            taskModel.addTask(newTitle.text, newNote.text, newCategory.text)
                            newTitle.clear()
                            newNote.clear()
                        }
                    }
                }
            }

            }
        }
    }


    footer: ToolBar {
        Label {
            id: statusText
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 12
            text: "Ready"
        }
    }

}
