#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "TaskListModel.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        TaskListModel taskModel;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("taskModel", &taskModel);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day12", "Main");
        return app.exec();
    }
