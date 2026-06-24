#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "Counter.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        Counter counter;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("counter", &counter);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day07", "Main");
        return app.exec();
    }
