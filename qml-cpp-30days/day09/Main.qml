import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 520
    visible: true
    title: "Day 09 - Calculator"

    ColumnLayout {
        anchors.centerIn: parent
        width: 420
        spacing: 12

        TextField { id: left; Layout.fillWidth: true; placeholderText: "左侧数字"; text: "12" }
        ComboBox { id: op; Layout.fillWidth: true; model: ["+", "-", "*", "/"] }
        TextField { id: right; Layout.fillWidth: true; placeholderText: "右侧数字"; text: "3" }
        Button {
            Layout.fillWidth: true
            text: "调用 C++ 计算"
            onClicked: result.text = calculator.calculate(Number(left.text), Number(right.text), op.currentText)
        }
        Label { id: result; text: "结果等待计算"; font.pixelSize: 26; font.bold: true }
    }
}
