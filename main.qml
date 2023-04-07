import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 640
    height: 480
    visible: true

    Text {
        anchors.centerIn: parent

        text: counter.value
    }

    Button {
        anchors {
            left: parent.left
            bottom: parent.bottom
            leftMargin: 8
            bottomMargin: 8
        }

        onClicked: counter.value -= 1

        text: "Decrement"

    }

    Button {
        anchors {
            right: parent.right
            bottom: parent.bottom
            rightMargin: 8
            bottomMargin: 8
        }

        onClicked: counter.value += 1

        text: "Increment"

    }
}
