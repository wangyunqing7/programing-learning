#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "Notifier.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        Notifier notifier;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("notifier", &notifier);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day08", "Main");
        return app.exec();
    }
