#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "TaskStore.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        TaskStore taskStore;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("taskStore", &taskStore);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day15", "Main");
        return app.exec();
    }
