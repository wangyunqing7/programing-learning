import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 500
    visible: true
    title: "Day 07 - Q_PROPERTY"

    ColumnLayout {
        anchors.centerIn: parent
        width: 420
        spacing: 16

        Label {
            Layout.alignment: Qt.AlignHCenter
            text: counter.value
            font.pixelSize: 56
            font.bold: true
        }

        ProgressBar {
            Layout.fillWidth: true
            from: 0
            to: 10
            value: Math.max(0, Math.min(counter.value, 10))
        }

        RowLayout {
            Layout.fillWidth: true
            Button { Layout.fillWidth: true; text: "-"; onClicked: counter.decrease() }
            Button { Layout.fillWidth: true; text: "重置"; onClicked: counter.reset() }
            Button { Layout.fillWidth: true; text: "+"; onClicked: counter.increase() }
        }
    }
}
