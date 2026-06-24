#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "TaskModel.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        TaskModel taskModel;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("taskModel", &taskModel);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day21", "Main");
        return app.exec();
    }
