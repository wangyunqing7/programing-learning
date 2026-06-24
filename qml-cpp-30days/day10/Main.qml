import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 820
    height: 560
    visible: true
    title: "Day 10 - QVariant Data"

    RowLayout {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 18

        Frame {
            Layout.fillWidth: true
            Layout.fillHeight: true
            ColumnLayout {
                anchors.fill: parent
                Label { text: "QStringList"; font.bold: true }
                Repeater {
                    model: bridge.skills()
                    delegate: Label { text: "• " + modelData }
                }
            }
        }

        Frame {
            Layout.fillWidth: true
            Layout.fillHeight: true
            ColumnLayout {
                anchors.fill: parent
                Label { text: "QVariantList<QVariantMap>"; font.bold: true }
                Repeater {
                    model: bridge.tasks()
                    delegate: Label { text: modelData.title + " / " + modelData.level }
                }
            }
        }
    }
}
