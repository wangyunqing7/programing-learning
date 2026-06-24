from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "qml-cpp-30days"


QT_PREFIX = "C:/Qt/6.11.1/mingw_64"
NINJA = "C:/Qt/Tools/Ninja/ninja.exe"
CXX = "C:/Qt/Tools/mingw1310_64/bin/g++.exe"


days_meta: list[dict[str, str]] = []


def clean_text(text: str) -> str:
    return dedent(text).strip() + "\n"


def write_file(relative: str, content: str) -> None:
    path = OUT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean_text(content), encoding="utf-8")


def day_dir(day: int) -> str:
    return f"day{day:02d}"


def day_uri(day: int) -> str:
    return f"Day{day:02d}"


def app_name(day: int) -> str:
    return f"appDay{day:02d}"


def cmake_for(day: int, sources: list[str] | None = None, qml_files: list[str] | None = None) -> str:
    sources = sources or []
    qml_files = qml_files or ["Main.qml"]
    source_lines = "\n    ".join(["main.cpp", *sources])
    qml_lines = "\n        ".join(qml_files)
    return f"""
    cmake_minimum_required(VERSION 3.21)
    project({day_uri(day)} LANGUAGES CXX)

    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_AUTOMOC ON)
    set(CMAKE_AUTORCC ON)

    find_package(Qt6 REQUIRED COMPONENTS Quick)
    qt_standard_project_setup(REQUIRES 6.8)

    qt_add_executable({app_name(day)}
        {source_lines}
    )

    qt_add_qml_module({app_name(day)}
        URI {day_uri(day)}
        VERSION 1.0
        QML_FILES
            {qml_lines}
    )

    target_link_libraries({app_name(day)} PRIVATE Qt6::Quick)
    """


def main_cpp(day: int, includes: str = "", before_engine: str = "", after_engine: str = "") -> str:
    return f"""
    #include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    {includes}

    int main(int argc, char *argv[])
    {{
        QGuiApplication app(argc, argv);
    {indent(before_engine, 4)}
        QQmlApplicationEngine engine;
    {indent(after_engine, 4)}
        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() {{ QCoreApplication::exit(-1); }},
            Qt::QueuedConnection);

        engine.loadFromModule("{day_uri(day)}", "Main");
        return app.exec();
    }}
    """


def indent(text: str, spaces: int) -> str:
    text = dedent(text).strip("\n")
    if not text:
        return ""
    pad = " " * spaces
    return "\n".join(pad + line if line else "" for line in text.splitlines()) + "\n"


def run_ps1(day: int) -> str:
    return f"""
    $ErrorActionPreference = "Stop"
    $env:Path = "C:\\Qt\\6.11.1\\mingw_64\\bin;C:\\Qt\\Tools\\mingw1310_64\\bin;C:\\Qt\\Tools\\Ninja;" + $env:Path

    $build = Join-Path $PSScriptRoot "build"
    cmake -S $PSScriptRoot -B $build -G Ninja -DCMAKE_PREFIX_PATH={QT_PREFIX} -DCMAKE_MAKE_PROGRAM={NINJA} -DCMAKE_CXX_COMPILER={CXX}
    cmake --build $build
    & (Join-Path $build "{app_name(day)}.exe")
    """


def docs_html(day: int, title: str, goal: str, concepts: list[str], files: list[str], exercise: str, tomorrow: str) -> str:
    days_meta.append({"day": f"{day:02d}", "title": title, "goal": goal})
    concept_items = "\n".join(f"<li>{html.escape(item)}</li>" for item in concepts)
    file_items = "\n".join(f"<li><code>{html.escape(item)}</code></li>" for item in files)
    command = f"""cd qml-cpp-30days/{day_dir(day)}
cmake -S . -B build -G Ninja -DCMAKE_PREFIX_PATH={QT_PREFIX} -DCMAKE_MAKE_PROGRAM={NINJA} -DCMAKE_CXX_COMPILER={CXX}
cmake --build build"""
    return f"""
    <!doctype html>
    <html lang="zh-CN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>第 {day:02d} 天 - {html.escape(title)}</title>
      <link rel="stylesheet" href="../assets/style.css">
    </head>
    <body>
      <main class="page">
        <nav class="topline"><a href="../index.html">返回目录</a><span>第 {day:02d} 天</span></nav>
        <h1>第 {day:02d} 天：{html.escape(title)}</h1>
        <section class="panel">
          <h2>今天目标</h2>
          <p>{html.escape(goal)}</p>
        </section>
        <section>
          <h2>核心概念</h2>
          <ul>{concept_items}</ul>
        </section>
        <section>
          <h2>项目文件</h2>
          <ul>{file_items}</ul>
        </section>
        <section>
          <h2>运行方式</h2>
          <p>在 PowerShell 中进入当天目录后执行下面命令，或者直接运行当天的 <code>run.ps1</code>。</p>
          <pre><code>{html.escape(command)}</code></pre>
        </section>
        <section>
          <h2>代码拆解</h2>
          <p>本日代码故意保持小而完整。先从 <code>Main.qml</code> 看界面结构，再看 <code>main.cpp</code> 如何加载 QML。包含 C++ 类的天数，再从头文件看暴露给 QML 的属性、方法和信号。</p>
          <p>QML 适合表达界面、状态和交互；C++ 适合保存数据、封装业务规则、提供模型，以及处理文件等系统能力。后面的完整 App 会持续强化这个分工。</p>
        </section>
        <section>
          <h2>常见错误</h2>
          <ul>
            <li>如果提示找不到 Qt，请确认 CMake 命令里带了 <code>-DCMAKE_PREFIX_PATH={QT_PREFIX}</code>。</li>
            <li>如果运行时提示缺少 DLL，请先把 <code>C:\\Qt\\6.11.1\\mingw_64\\bin</code> 加入当前 PowerShell 的 <code>PATH</code>。</li>
            <li>如果改了 C++ 头文件但界面没变化，先重新构建，因为 <code>Q_OBJECT</code> 需要 moc 重新生成元对象代码。</li>
          </ul>
        </section>
        <section>
          <h2>今日练习</h2>
          <p>{html.escape(exercise)}</p>
        </section>
        <section class="next">
          <h2>明天预告</h2>
          <p>{html.escape(tomorrow)}</p>
        </section>
      </main>
    </body>
    </html>
    """


def write_day(day: int, title: str, goal: str, concepts: list[str], exercise: str, tomorrow: str, files: dict[str, str]) -> None:
    rel = day_dir(day)
    if "CMakeLists.txt" not in files:
        raise ValueError(f"Day {day} is missing CMakeLists.txt")
    if "main.cpp" not in files:
        raise ValueError(f"Day {day} is missing main.cpp")
    if "Main.qml" not in files:
        raise ValueError(f"Day {day} is missing Main.qml")

    for name, content in files.items():
        write_file(f"{rel}/{name}", content)
    write_file(f"{rel}/run.ps1", run_ps1(day))
    write_file(f"{rel}/docs.html", docs_html(day, title, goal, concepts, sorted(files.keys()) + ["run.ps1", "docs.html"], exercise, tomorrow))


def message_provider_files() -> dict[str, str]:
    return {
        "MessageProvider.h": """
        #ifndef MESSAGEPROVIDER_H
        #define MESSAGEPROVIDER_H

        #include <QObject>
        #include <QString>

        class MessageProvider : public QObject
        {
            Q_OBJECT
        public:
            explicit MessageProvider(QObject *parent = nullptr);

            Q_INVOKABLE QString greeting(const QString &name) const;
            Q_INVOKABLE QString todayTopic() const;
        };

        #endif
        """,
        "MessageProvider.cpp": """
        #include "MessageProvider.h"

        MessageProvider::MessageProvider(QObject *parent)
            : QObject(parent)
        {
        }

        QString MessageProvider::greeting(const QString &name) const
        {
            const QString trimmed = name.trimmed();
            if (trimmed.isEmpty()) {
                return QStringLiteral("你好，QML 学习者。");
            }
            return QStringLiteral("你好，%1。这个字符串来自 C++。").arg(trimmed);
        }

        QString MessageProvider::todayTopic() const
        {
            return QStringLiteral("今天练习 QML 调用 C++ 对象的方法。");
        }
        """,
    }


def counter_files() -> dict[str, str]:
    return {
        "Counter.h": """
        #ifndef COUNTER_H
        #define COUNTER_H

        #include <QObject>

        class Counter : public QObject
        {
            Q_OBJECT
            Q_PROPERTY(int value READ value WRITE setValue NOTIFY valueChanged)

        public:
            explicit Counter(QObject *parent = nullptr);

            int value() const;
            void setValue(int value);

            Q_INVOKABLE void increase();
            Q_INVOKABLE void decrease();
            Q_INVOKABLE void reset();

        signals:
            void valueChanged();

        private:
            int m_value = 0;
        };

        #endif
        """,
        "Counter.cpp": """
        #include "Counter.h"

        Counter::Counter(QObject *parent)
            : QObject(parent)
        {
        }

        int Counter::value() const
        {
            return m_value;
        }

        void Counter::setValue(int value)
        {
            if (m_value == value) {
                return;
            }
            m_value = value;
            emit valueChanged();
        }

        void Counter::increase()
        {
            setValue(m_value + 1);
        }

        void Counter::decrease()
        {
            setValue(m_value - 1);
        }

        void Counter::reset()
        {
            setValue(0);
        }
        """,
    }


def notifier_files() -> dict[str, str]:
    return {
        "Notifier.h": """
        #ifndef NOTIFIER_H
        #define NOTIFIER_H

        #include <QObject>
        #include <QString>

        class Notifier : public QObject
        {
            Q_OBJECT
        public:
            explicit Notifier(QObject *parent = nullptr);

            Q_INVOKABLE void sendNotice(const QString &text);

        signals:
            void notice(const QString &message);
        };

        #endif
        """,
        "Notifier.cpp": """
        #include "Notifier.h"

        Notifier::Notifier(QObject *parent)
            : QObject(parent)
        {
        }

        void Notifier::sendNotice(const QString &text)
        {
            const QString message = text.trimmed().isEmpty()
                ? QStringLiteral("C++ 发出了一条默认通知")
                : QStringLiteral("C++ 通知：%1").arg(text.trimmed());
            emit notice(message);
        }
        """,
    }


def calculator_files() -> dict[str, str]:
    return {
        "Calculator.h": """
        #ifndef CALCULATOR_H
        #define CALCULATOR_H

        #include <QObject>
        #include <QString>

        class Calculator : public QObject
        {
            Q_OBJECT
        public:
            explicit Calculator(QObject *parent = nullptr);

            Q_INVOKABLE double calculate(double left, double right, const QString &op) const;
        };

        #endif
        """,
        "Calculator.cpp": """
        #include "Calculator.h"

        Calculator::Calculator(QObject *parent)
            : QObject(parent)
        {
        }

        double Calculator::calculate(double left, double right, const QString &op) const
        {
            if (op == QStringLiteral("+")) {
                return left + right;
            }
            if (op == QStringLiteral("-")) {
                return left - right;
            }
            if (op == QStringLiteral("*")) {
                return left * right;
            }
            if (op == QStringLiteral("/") && right != 0.0) {
                return left / right;
            }
            return 0.0;
        }
        """,
    }


def data_bridge_files() -> dict[str, str]:
    return {
        "DataBridge.h": """
        #ifndef DATABRIDGE_H
        #define DATABRIDGE_H

        #include <QObject>
        #include <QStringList>
        #include <QVariantList>

        class DataBridge : public QObject
        {
            Q_OBJECT
        public:
            explicit DataBridge(QObject *parent = nullptr);

            Q_INVOKABLE QStringList skills() const;
            Q_INVOKABLE QVariantList tasks() const;
        };

        #endif
        """,
        "DataBridge.cpp": """
        #include "DataBridge.h"

        #include <QVariantMap>

        DataBridge::DataBridge(QObject *parent)
            : QObject(parent)
        {
        }

        QStringList DataBridge::skills() const
        {
            return {
                QStringLiteral("QML 属性"),
                QStringLiteral("C++ 方法"),
                QStringLiteral("QVariant 数据")
            };
        }

        QVariantList DataBridge::tasks() const
        {
            QVariantList list;
            list << QVariantMap{{QStringLiteral("title"), QStringLiteral("读取 QVariantList")},
                                 {QStringLiteral("level"), QStringLiteral("基础")}};
            list << QVariantMap{{QStringLiteral("title"), QStringLiteral("在 QML 中显示 Map 字段")},
                                 {QStringLiteral("level"), QStringLiteral("练习")}};
            list << QVariantMap{{QStringLiteral("title"), QStringLiteral("准备学习模型")},
                                 {QStringLiteral("level"), QStringLiteral("进阶")}};
            return list;
        }
        """,
    }


def simple_task_model_files(class_name: str = "TaskListModel") -> dict[str, str]:
    return {
        f"{class_name}.h": f"""
        #ifndef {class_name.upper()}_H
        #define {class_name.upper()}_H

        #include <QAbstractListModel>
        #include <QString>
        #include <QVector>

        class {class_name} : public QAbstractListModel
        {{
            Q_OBJECT
        public:
            enum Roles {{
                TitleRole = Qt::UserRole + 1,
                DoneRole
            }};

            explicit {class_name}(QObject *parent = nullptr);

            int rowCount(const QModelIndex &parent = QModelIndex()) const override;
            QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
            QHash<int, QByteArray> roleNames() const override;

            Q_INVOKABLE void addTask(const QString &title);
            Q_INVOKABLE void toggleDone(int row);
            Q_INVOKABLE void removeTask(int row);

        private:
            struct Task {{
                QString title;
                bool done = false;
            }};

            QVector<Task> m_tasks;
        }};

        #endif
        """,
        f"{class_name}.cpp": f"""
        #include "{class_name}.h"

        {class_name}::{class_name}(QObject *parent)
            : QAbstractListModel(parent)
        {{
            m_tasks = {{
                {{QStringLiteral("理解 roleNames"), false}},
                {{QStringLiteral("把 C++ 模型绑定到 ListView"), false}},
                {{QStringLiteral("从 QML 调用模型方法"), true}}
            }};
        }}

        int {class_name}::rowCount(const QModelIndex &parent) const
        {{
            if (parent.isValid()) {{
                return 0;
            }}
            return m_tasks.size();
        }}

        QVariant {class_name}::data(const QModelIndex &index, int role) const
        {{
            if (!index.isValid() || index.row() < 0 || index.row() >= m_tasks.size()) {{
                return {{}};
            }}

            const Task &task = m_tasks.at(index.row());
            if (role == TitleRole) {{
                return task.title;
            }}
            if (role == DoneRole) {{
                return task.done;
            }}
            return {{}};
        }}

        QHash<int, QByteArray> {class_name}::roleNames() const
        {{
            return {{
                {{TitleRole, "title"}},
                {{DoneRole, "done"}}
            }};
        }}

        void {class_name}::addTask(const QString &title)
        {{
            const QString cleanTitle = title.trimmed();
            if (cleanTitle.isEmpty()) {{
                return;
            }}

            const int row = m_tasks.size();
            beginInsertRows(QModelIndex(), row, row);
            m_tasks.append({{cleanTitle, false}});
            endInsertRows();
        }}

        void {class_name}::toggleDone(int row)
        {{
            if (row < 0 || row >= m_tasks.size()) {{
                return;
            }}
            m_tasks[row].done = !m_tasks[row].done;
            const QModelIndex changed = index(row, 0);
            emit dataChanged(changed, changed, {{DoneRole}});
        }}

        void {class_name}::removeTask(int row)
        {{
            if (row < 0 || row >= m_tasks.size()) {{
                return;
            }}
            beginRemoveRows(QModelIndex(), row, row);
            m_tasks.removeAt(row);
            endRemoveRows();
        }}
        """,
    }


def json_store_files() -> dict[str, str]:
    return {
        "JsonStore.h": """
        #ifndef JSONSTORE_H
        #define JSONSTORE_H

        #include <QObject>
        #include <QVariantList>

        class JsonStore : public QObject
        {
            Q_OBJECT
            Q_PROPERTY(QVariantList items READ items NOTIFY itemsChanged)

        public:
            explicit JsonStore(QObject *parent = nullptr);

            QVariantList items() const;

            Q_INVOKABLE bool load();
            Q_INVOKABLE bool save() const;
            Q_INVOKABLE void addItem(const QString &title);

        signals:
            void itemsChanged();

        private:
            QString filePath() const;
            QVariantList m_items;
        };

        #endif
        """,
        "JsonStore.cpp": """
        #include "JsonStore.h"

        #include <QDir>
        #include <QFile>
        #include <QJsonArray>
        #include <QJsonDocument>
        #include <QJsonObject>
        #include <QStandardPaths>
        #include <QVariantMap>

        JsonStore::JsonStore(QObject *parent)
            : QObject(parent)
        {
            load();
        }

        QVariantList JsonStore::items() const
        {
            return m_items;
        }

        bool JsonStore::load()
        {
            QFile file(filePath());
            if (!file.exists()) {
                m_items = {
                    QVariantMap{{QStringLiteral("title"), QStringLiteral("第一条本地数据")}},
                    QVariantMap{{QStringLiteral("title"), QStringLiteral("保存后再次启动仍然存在")}}
                };
                emit itemsChanged();
                return save();
            }

            if (!file.open(QIODevice::ReadOnly)) {
                return false;
            }

            const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
            QVariantList loaded;
            for (const QJsonValue &value : document.array()) {
                loaded.append(value.toObject().toVariantMap());
            }
            m_items = loaded;
            emit itemsChanged();
            return true;
        }

        bool JsonStore::save() const
        {
            const QString path = filePath();
            QDir().mkpath(QFileInfo(path).absolutePath());

            QJsonArray array;
            for (const QVariant &item : m_items) {
                array.append(QJsonObject::fromVariantMap(item.toMap()));
            }

            QFile file(path);
            if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
                return false;
            }
            file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
            return true;
        }

        void JsonStore::addItem(const QString &title)
        {
            const QString cleanTitle = title.trimmed();
            if (cleanTitle.isEmpty()) {
                return;
            }
            m_items.append(QVariantMap{{QStringLiteral("title"), cleanTitle}});
            emit itemsChanged();
            save();
        }

        QString JsonStore::filePath() const
        {
            const QString base = QStandardPaths::writableLocation(QStandardPaths::AppDataLocation);
            return base + QStringLiteral("/day14-items.json");
        }
        """,
    }


def task_store_files() -> dict[str, str]:
    return {
        "TaskStore.h": """
        #ifndef TASKSTORE_H
        #define TASKSTORE_H

        #include <QObject>
        #include <QVariantList>

        class TaskStore : public QObject
        {
            Q_OBJECT
            Q_PROPERTY(QVariantList tasks READ tasks NOTIFY tasksChanged)

        public:
            explicit TaskStore(QObject *parent = nullptr);

            QVariantList tasks() const;

            Q_INVOKABLE void addTask(const QString &title);
            Q_INVOKABLE void toggleTask(int row);
            Q_INVOKABLE void removeTask(int row);
            Q_INVOKABLE bool load();
            Q_INVOKABLE bool save() const;

        signals:
            void tasksChanged();

        private:
            QString filePath() const;
            QVariantList m_tasks;
        };

        #endif
        """,
        "TaskStore.cpp": """
        #include "TaskStore.h"

        #include <QDir>
        #include <QFile>
        #include <QFileInfo>
        #include <QJsonArray>
        #include <QJsonDocument>
        #include <QJsonObject>
        #include <QStandardPaths>
        #include <QVariantMap>

        TaskStore::TaskStore(QObject *parent)
            : QObject(parent)
        {
            load();
        }

        QVariantList TaskStore::tasks() const
        {
            return m_tasks;
        }

        void TaskStore::addTask(const QString &title)
        {
            const QString cleanTitle = title.trimmed();
            if (cleanTitle.isEmpty()) {
                return;
            }
            m_tasks.append(QVariantMap{{QStringLiteral("title"), cleanTitle},
                                       {QStringLiteral("done"), false}});
            emit tasksChanged();
            save();
        }

        void TaskStore::toggleTask(int row)
        {
            if (row < 0 || row >= m_tasks.size()) {
                return;
            }
            QVariantMap task = m_tasks.at(row).toMap();
            task[QStringLiteral("done")] = !task.value(QStringLiteral("done")).toBool();
            m_tasks[row] = task;
            emit tasksChanged();
            save();
        }

        void TaskStore::removeTask(int row)
        {
            if (row < 0 || row >= m_tasks.size()) {
                return;
            }
            m_tasks.removeAt(row);
            emit tasksChanged();
            save();
        }

        bool TaskStore::load()
        {
            QFile file(filePath());
            if (!file.exists()) {
                m_tasks = {
                    QVariantMap{{QStringLiteral("title"), QStringLiteral("完成第 15 天综合练习")},
                                {QStringLiteral("done"), false}},
                    QVariantMap{{QStringLiteral("title"), QStringLiteral("准备进入完整 App 阶段")},
                                {QStringLiteral("done"), false}}
                };
                emit tasksChanged();
                return save();
            }

            if (!file.open(QIODevice::ReadOnly)) {
                return false;
            }
            const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
            QVariantList loaded;
            for (const QJsonValue &value : document.array()) {
                loaded.append(value.toObject().toVariantMap());
            }
            m_tasks = loaded;
            emit tasksChanged();
            return true;
        }

        bool TaskStore::save() const
        {
            const QString path = filePath();
            QDir().mkpath(QFileInfo(path).absolutePath());

            QJsonArray array;
            for (const QVariant &task : m_tasks) {
                array.append(QJsonObject::fromVariantMap(task.toMap()));
            }

            QFile file(path);
            if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
                return false;
            }
            file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
            return true;
        }

        QString TaskStore::filePath() const
        {
            return QStandardPaths::writableLocation(QStandardPaths::AppDataLocation)
                + QStringLiteral("/day15-tasks.json");
        }
        """,
    }


def task_model_final_files() -> dict[str, str]:
    return {
        "TaskModel.h": """
        #ifndef TASKMODEL_H
        #define TASKMODEL_H

        #include <QAbstractListModel>
        #include <QString>
        #include <QVariantMap>
        #include <QVector>

        class TaskModel : public QAbstractListModel
        {
            Q_OBJECT
            Q_PROPERTY(QString filterText READ filterText WRITE setFilterText NOTIFY filterChanged)
            Q_PROPERTY(QString filterCategory READ filterCategory WRITE setFilterCategory NOTIFY filterChanged)
            Q_PROPERTY(int totalCount READ totalCount NOTIFY countChanged)
            Q_PROPERTY(int visibleCount READ visibleCount NOTIFY countChanged)
            Q_PROPERTY(int completedCount READ completedCount NOTIFY countChanged)

        public:
            enum Roles {
                TitleRole = Qt::UserRole + 1,
                NoteRole,
                CategoryRole,
                DoneRole,
                CreatedAtRole
            };

            explicit TaskModel(QObject *parent = nullptr);

            int rowCount(const QModelIndex &parent = QModelIndex()) const override;
            QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
            QHash<int, QByteArray> roleNames() const override;

            QString filterText() const;
            void setFilterText(const QString &text);
            QString filterCategory() const;
            void setFilterCategory(const QString &category);

            int totalCount() const;
            int visibleCount() const;
            int completedCount() const;

            Q_INVOKABLE QVariantMap get(int row) const;
            Q_INVOKABLE void addTask(const QString &title, const QString &note, const QString &category);
            Q_INVOKABLE void removeTask(int row);
            Q_INVOKABLE void updateTask(int row, const QString &title, const QString &note, const QString &category);
            Q_INVOKABLE void toggleDone(int row);
            Q_INVOKABLE void clearCompleted();
            Q_INVOKABLE bool save() const;
            Q_INVOKABLE bool load();
            Q_INVOKABLE bool exportTo(const QString &fileName) const;
            Q_INVOKABLE bool importFrom(const QString &fileName);

        signals:
            void filterChanged();
            void countChanged();

        private:
            struct Task {
                QString title;
                QString note;
                QString category;
                bool done = false;
                QString createdAt;
            };

            QVector<Task> m_tasks;
            QVector<int> m_visibleRows;
            QString m_filterText;
            QString m_filterCategory;

            void seed();
            void rebuildVisibleRows();
            int sourceRowForVisibleRow(int row) const;
            QString storagePath() const;
            QString documentPath(const QString &fileName) const;
            QJsonObject toJson(const Task &task) const;
            Task fromJson(const QJsonObject &object) const;
        };

        #endif
        """,
        "TaskModel.cpp": """
        #include "TaskModel.h"

        #include <QDateTime>
        #include <QDir>
        #include <QFile>
        #include <QFileInfo>
        #include <QJsonArray>
        #include <QJsonDocument>
        #include <QJsonObject>
        #include <QStandardPaths>

        TaskModel::TaskModel(QObject *parent)
            : QAbstractListModel(parent)
        {
            seed();
            rebuildVisibleRows();
        }

        int TaskModel::rowCount(const QModelIndex &parent) const
        {
            if (parent.isValid()) {
                return 0;
            }
            return m_visibleRows.size();
        }

        QVariant TaskModel::data(const QModelIndex &index, int role) const
        {
            if (!index.isValid()) {
                return {};
            }

            const int sourceRow = sourceRowForVisibleRow(index.row());
            if (sourceRow < 0) {
                return {};
            }

            const Task &task = m_tasks.at(sourceRow);
            switch (role) {
            case TitleRole:
                return task.title;
            case NoteRole:
                return task.note;
            case CategoryRole:
                return task.category;
            case DoneRole:
                return task.done;
            case CreatedAtRole:
                return task.createdAt;
            default:
                return {};
            }
        }

        QHash<int, QByteArray> TaskModel::roleNames() const
        {
            return {
                {TitleRole, "title"},
                {NoteRole, "note"},
                {CategoryRole, "category"},
                {DoneRole, "done"},
                {CreatedAtRole, "createdAt"}
            };
        }

        QString TaskModel::filterText() const
        {
            return m_filterText;
        }

        void TaskModel::setFilterText(const QString &text)
        {
            if (m_filterText == text) {
                return;
            }
            m_filterText = text;
            rebuildVisibleRows();
            emit filterChanged();
            emit countChanged();
        }

        QString TaskModel::filterCategory() const
        {
            return m_filterCategory;
        }

        void TaskModel::setFilterCategory(const QString &category)
        {
            if (m_filterCategory == category) {
                return;
            }
            m_filterCategory = category;
            rebuildVisibleRows();
            emit filterChanged();
            emit countChanged();
        }

        int TaskModel::totalCount() const
        {
            return m_tasks.size();
        }

        int TaskModel::visibleCount() const
        {
            return m_visibleRows.size();
        }

        int TaskModel::completedCount() const
        {
            int count = 0;
            for (const Task &task : m_tasks) {
                if (task.done) {
                    ++count;
                }
            }
            return count;
        }

        QVariantMap TaskModel::get(int row) const
        {
            const int sourceRow = sourceRowForVisibleRow(row);
            if (sourceRow < 0) {
                return {};
            }
            const Task &task = m_tasks.at(sourceRow);
            return {
                {QStringLiteral("title"), task.title},
                {QStringLiteral("note"), task.note},
                {QStringLiteral("category"), task.category},
                {QStringLiteral("done"), task.done},
                {QStringLiteral("createdAt"), task.createdAt}
            };
        }

        void TaskModel::addTask(const QString &title, const QString &note, const QString &category)
        {
            const QString cleanTitle = title.trimmed();
            if (cleanTitle.isEmpty()) {
                return;
            }

            Task task;
            task.title = cleanTitle;
            task.note = note.trimmed();
            task.category = category.trimmed().isEmpty() ? QStringLiteral("默认") : category.trimmed();
            task.done = false;
            task.createdAt = QDateTime::currentDateTime().toString(Qt::ISODate);

            m_tasks.append(task);
            rebuildVisibleRows();
            emit countChanged();
        }

        void TaskModel::removeTask(int row)
        {
            const int sourceRow = sourceRowForVisibleRow(row);
            if (sourceRow < 0) {
                return;
            }
            m_tasks.removeAt(sourceRow);
            rebuildVisibleRows();
            emit countChanged();
        }

        void TaskModel::updateTask(int row, const QString &title, const QString &note, const QString &category)
        {
            const int sourceRow = sourceRowForVisibleRow(row);
            if (sourceRow < 0 || title.trimmed().isEmpty()) {
                return;
            }
            Task &task = m_tasks[sourceRow];
            task.title = title.trimmed();
            task.note = note.trimmed();
            task.category = category.trimmed().isEmpty() ? QStringLiteral("默认") : category.trimmed();
            rebuildVisibleRows();
            emit countChanged();
        }

        void TaskModel::toggleDone(int row)
        {
            const int sourceRow = sourceRowForVisibleRow(row);
            if (sourceRow < 0) {
                return;
            }
            m_tasks[sourceRow].done = !m_tasks[sourceRow].done;
            const QModelIndex changed = index(row, 0);
            emit dataChanged(changed, changed, {DoneRole});
            emit countChanged();
        }

        void TaskModel::clearCompleted()
        {
            for (int i = m_tasks.size() - 1; i >= 0; --i) {
                if (m_tasks.at(i).done) {
                    m_tasks.removeAt(i);
                }
            }
            rebuildVisibleRows();
            emit countChanged();
        }

        bool TaskModel::save() const
        {
            const QString path = storagePath();
            QDir().mkpath(QFileInfo(path).absolutePath());

            QJsonArray array;
            for (const Task &task : m_tasks) {
                array.append(toJson(task));
            }

            QFile file(path);
            if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
                return false;
            }
            file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
            return true;
        }

        bool TaskModel::load()
        {
            QFile file(storagePath());
            if (!file.exists()) {
                return save();
            }
            if (!file.open(QIODevice::ReadOnly)) {
                return false;
            }

            const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
            QVector<Task> loaded;
            for (const QJsonValue &value : document.array()) {
                loaded.append(fromJson(value.toObject()));
            }
            if (!loaded.isEmpty()) {
                m_tasks = loaded;
                rebuildVisibleRows();
                emit countChanged();
            }
            return true;
        }

        bool TaskModel::exportTo(const QString &fileName) const
        {
            const QString path = documentPath(fileName.trimmed().isEmpty()
                ? QStringLiteral("qml-cpp-tasks-export.json")
                : fileName.trimmed());
            QDir().mkpath(QFileInfo(path).absolutePath());

            QJsonArray array;
            for (const Task &task : m_tasks) {
                array.append(toJson(task));
            }

            QFile file(path);
            if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
                return false;
            }
            file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
            return true;
        }

        bool TaskModel::importFrom(const QString &fileName)
        {
            const QString path = documentPath(fileName.trimmed().isEmpty()
                ? QStringLiteral("qml-cpp-tasks-export.json")
                : fileName.trimmed());
            QFile file(path);
            if (!file.open(QIODevice::ReadOnly)) {
                return false;
            }

            const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
            QVector<Task> imported;
            for (const QJsonValue &value : document.array()) {
                imported.append(fromJson(value.toObject()));
            }
            if (imported.isEmpty()) {
                return false;
            }
            m_tasks = imported;
            rebuildVisibleRows();
            emit countChanged();
            return true;
        }

        void TaskModel::seed()
        {
            m_tasks = {
                {QStringLiteral("建立 QML + C++ App 框架"), QStringLiteral("界面由 QML 负责，数据由 C++ 模型负责。"), QStringLiteral("学习"), false, QDateTime::currentDateTime().toString(Qt::ISODate)},
                {QStringLiteral("实现任务增删改查"), QStringLiteral("通过 Q_INVOKABLE 暴露方法给 QML。"), QStringLiteral("功能"), false, QDateTime::currentDateTime().toString(Qt::ISODate)},
                {QStringLiteral("保存到 JSON 文件"), QStringLiteral("用 QJsonDocument 进行本地持久化。"), QStringLiteral("数据"), true, QDateTime::currentDateTime().toString(Qt::ISODate)}
            };
        }

        void TaskModel::rebuildVisibleRows()
        {
            beginResetModel();
            m_visibleRows.clear();
            for (int i = 0; i < m_tasks.size(); ++i) {
                const Task &task = m_tasks.at(i);
                const bool textMatches = m_filterText.trimmed().isEmpty()
                    || task.title.contains(m_filterText, Qt::CaseInsensitive)
                    || task.note.contains(m_filterText, Qt::CaseInsensitive);
                const bool categoryMatches = m_filterCategory.trimmed().isEmpty()
                    || m_filterCategory == QStringLiteral("全部")
                    || task.category.compare(m_filterCategory, Qt::CaseInsensitive) == 0;
                if (textMatches && categoryMatches) {
                    m_visibleRows.append(i);
                }
            }
            endResetModel();
        }

        int TaskModel::sourceRowForVisibleRow(int row) const
        {
            if (row < 0 || row >= m_visibleRows.size()) {
                return -1;
            }
            return m_visibleRows.at(row);
        }

        QString TaskModel::storagePath() const
        {
            return QStandardPaths::writableLocation(QStandardPaths::AppDataLocation)
                + QStringLiteral("/tasks.json");
        }

        QString TaskModel::documentPath(const QString &fileName) const
        {
            QFileInfo info(fileName);
            if (info.isAbsolute()) {
                return fileName;
            }
            return QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation)
                + QStringLiteral("/") + fileName;
        }

        QJsonObject TaskModel::toJson(const Task &task) const
        {
            return {
                {QStringLiteral("title"), task.title},
                {QStringLiteral("note"), task.note},
                {QStringLiteral("category"), task.category},
                {QStringLiteral("done"), task.done},
                {QStringLiteral("createdAt"), task.createdAt}
            };
        }

        TaskModel::Task TaskModel::fromJson(const QJsonObject &object) const
        {
            Task task;
            task.title = object.value(QStringLiteral("title")).toString();
            task.note = object.value(QStringLiteral("note")).toString();
            task.category = object.value(QStringLiteral("category")).toString(QStringLiteral("默认"));
            task.done = object.value(QStringLiteral("done")).toBool(false);
            task.createdAt = object.value(QStringLiteral("createdAt")).toString(QDateTime::currentDateTime().toString(Qt::ISODate));
            return task;
        }
        """,
    }


def final_app_qml(day: int, title: str) -> str:
    can_add = day >= 18
    can_delete = day >= 19
    can_edit = day >= 20
    can_done = day >= 21
    can_filter = day >= 22
    can_category = day >= 23
    can_persist = day >= 25
    can_empty = day >= 26
    can_polish = day >= 27
    can_import = day >= 28

    completed_button = """
                    Button {
                        text: "切换完成"
                        enabled: taskList.currentIndex >= 0
                        onClicked: taskModel.toggleDone(taskList.currentIndex)
                    }
    """ if can_done else ""

    delete_button = """
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
    """ if can_delete else ""

    edit_button = """
                    Button {
                        text: "保存修改"
                        enabled: taskList.currentIndex >= 0 && titleField.text.trim().length > 0
                        onClicked: taskModel.updateTask(taskList.currentIndex, titleField.text, noteField.text, categoryField.text)
                    }
    """ if can_edit else ""

    add_panel = """
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
                            visible: CATEGORY_VISIBLE
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
    """.replace("CATEGORY_VISIBLE", "true" if can_category else "false") if can_add else ""

    filter_panel = """
                Frame {
                    Layout.fillWidth: true
                    ColumnLayout {
                        anchors.fill: parent
                        spacing: 8
                        Label { text: "筛选"; font.bold: true }
                        TextField {
                            Layout.fillWidth: true
                            placeholderText: "搜索标题或笔记"
                            onTextChanged: taskModel.filterText = text
                        }
                        ComboBox {
                            Layout.fillWidth: true
                            model: ["全部", "学习", "功能", "数据", "默认"]
                            onActivated: taskModel.filterCategory = currentText
                            visible: CATEGORY_VISIBLE
                        }
                    }
                }
    """.replace("CATEGORY_VISIBLE", "true" if can_category else "false") if can_filter else ""

    persist_buttons = """
                    Button {
                        text: "保存 JSON"
                        onClicked: statusText.text = taskModel.save() ? "已保存到应用数据目录" : "保存失败"
                    }
                    Button {
                        text: "重新加载"
                        onClicked: statusText.text = taskModel.load() ? "已重新加载" : "加载失败"
                    }
    """ if can_persist else ""

    import_buttons = """
                    Button {
                        text: "导出"
                        onClicked: statusText.text = taskModel.exportTo("qml-cpp-tasks-export.json") ? "已导出到文档目录" : "导出失败"
                    }
                    Button {
                        text: "导入"
                        onClicked: statusText.text = taskModel.importFrom("qml-cpp-tasks-export.json") ? "已从文档目录导入" : "导入失败"
                    }
    """ if can_import else ""

    empty_state = """
                Label {
                    Layout.fillWidth: true
                    visible: taskModel.visibleCount === 0
                    text: "没有匹配的任务。可以清空筛选条件，或新增一条任务。"
                    color: "#64748b"
                    wrapMode: Text.WordWrap
                }
    """ if can_empty else ""

    footer = """
        footer: ToolBar {
            RowLayout {
                anchors.fill: parent
                Label {
                    Layout.leftMargin: 12
                    text: "总数 " + taskModel.totalCount + "，当前显示 " + taskModel.visibleCount + "，已完成 " + taskModel.completedCount
                }
                Item { Layout.fillWidth: true }
                Label {
                    id: statusText
                    Layout.rightMargin: 12
                    text: "Ready"
                    color: "#475569"
                }
            }
        }
    """ if can_polish else """
        footer: ToolBar {
            Label {
                id: statusText
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 12
                text: "Ready"
            }
        }
    """

    on_completed = "taskModel.load()" if can_persist else ""

    return f"""
    import QtQuick
    import QtQuick.Controls
    import QtQuick.Layouts

    ApplicationWindow {{
        id: window
        width: 1040
        height: 680
        visible: true
        title: "第 {day:02d} 天 - {title}"

        Component.onCompleted: {{
            {on_completed}
        }}

        header: ToolBar {{
            RowLayout {{
                anchors.fill: parent
                Label {{
                    Layout.leftMargin: 12
                    text: "任务 / 笔记管理"
                    font.bold: true
                    font.pixelSize: 18
                }}
                Item {{ Layout.fillWidth: true }}
                Label {{
                    Layout.rightMargin: 12
                    text: "Day {day:02d}"
                    color: "#475569"
                }}
            }}
        }}

        SplitView {{
            anchors.fill: parent
            orientation: Qt.Horizontal

            Frame {{
                SplitView.preferredWidth: 340
                SplitView.minimumWidth: 280
                ColumnLayout {{
                    anchors.fill: parent
                    spacing: 10

                    Label {{
                        text: "任务列表"
                        font.bold: true
                        font.pixelSize: 16
                    }}

                    {filter_panel}

                    ListView {{
                        id: taskList
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        clip: true
                        model: taskModel
                        delegate: ItemDelegate {{
                            width: taskList.width
                            text: (done ? "✓ " : "□ ") + title
                            highlighted: ListView.isCurrentItem
                            onClicked: {{
                                taskList.currentIndex = index
                                const item = taskModel.get(index)
                                titleField.text = item.title || ""
                                noteField.text = item.note || ""
                                categoryField.text = item.category || "默认"
                            }}
                        }}
                    }}

                    {empty_state}
                }}
            }}

            Frame {{
                SplitView.fillWidth: true
                ColumnLayout {{
                    anchors.fill: parent
                    spacing: 12

                    Label {{
                        text: "详情"
                        font.bold: true
                        font.pixelSize: 16
                    }}

                    TextField {{
                        id: titleField
                        Layout.fillWidth: true
                        placeholderText: "选择左侧任务后显示标题"
                        readOnly: {"false" if can_edit else "true"}
                    }}

                    TextArea {{
                        id: noteField
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        placeholderText: "任务说明或笔记"
                        readOnly: {"false" if can_edit else "true"}
                        wrapMode: TextArea.Wrap
                    }}

                    TextField {{
                        id: categoryField
                        Layout.fillWidth: true
                        placeholderText: "分类"
                        text: "默认"
                        visible: {"true" if can_category else "false"}
                        readOnly: {"false" if can_edit else "true"}
                    }}

                    RowLayout {{
                        Layout.fillWidth: true
                        {completed_button}
                        {edit_button}
                        {delete_button}
                        {persist_buttons}
                        {import_buttons}
                        Item {{ Layout.fillWidth: true }}
                    }}

                    {add_panel}
                }}
            }}
        }}

        {footer}
    }}
    """


def generate_basic_days() -> None:
    write_day(
        1,
        "第一个 Qt Quick 窗口",
        "建立最小 QML 项目，理解 C++ 程序如何加载 QML 界面。",
        ["QGuiApplication 是 Qt Quick 程序入口", "QQmlApplicationEngine 负责加载 QML 模块", "Window 是最简单的顶层窗口"],
        "把窗口标题、背景色和主标题文字改成你自己的内容。",
        "学习属性、绑定和鼠标事件。",
        {
            "CMakeLists.txt": cmake_for(1),
            "main.cpp": main_cpp(1),
            "Main.qml": """
            import QtQuick

            Window {
                width: 720
                height: 480
                visible: true
                title: "Day 01 - Hello QML"

                Rectangle {
                    anchors.fill: parent
                    color: "#f8fafc"

                    Column {
                        anchors.centerIn: parent
                        spacing: 14

                        Text {
                            text: "Hello QML"
                            font.pixelSize: 40
                            font.bold: true
                            color: "#0f172a"
                        }

                        Text {
                            text: "这是第一个由 C++ 加载的 Qt Quick 窗口"
                            font.pixelSize: 18
                            color: "#475569"
                        }
                    }
                }
            }
            """,
        },
    )

    write_day(
        2,
        "属性、绑定和点击事件",
        "用 QML 属性保存状态，用绑定自动刷新界面，用 MouseArea 接收点击。",
        ["property 定义本地状态", "绑定表达式会跟随依赖自动更新", "MouseArea 可以把普通图形变成可点击区域"],
        "把点击次数改成影响字体大小或卡片圆角。",
        "学习组件拆分和布局组织。",
        {
            "CMakeLists.txt": cmake_for(2),
            "main.cpp": main_cpp(2),
            "Main.qml": """
            import QtQuick

            Window {
                id: window
                width: 720
                height: 480
                visible: true
                title: "Day 02 - Binding"

                property int clickCount: 0

                Rectangle {
                    anchors.fill: parent
                    color: clickCount % 2 === 0 ? "#eff6ff" : "#f0fdf4"

                    Rectangle {
                        id: card
                        width: 360
                        height: 220
                        radius: 16
                        anchors.centerIn: parent
                        color: "white"
                        border.color: "#cbd5e1"

                        Column {
                            anchors.centerIn: parent
                            spacing: 14

                            Text {
                                text: "点击次数：" + window.clickCount
                                font.pixelSize: 30
                                font.bold: true
                                color: "#0f172a"
                            }

                            Text {
                                text: window.clickCount >= 5 ? "绑定正在自动更新" : "点击卡片试试看"
                                font.pixelSize: 18
                                color: "#64748b"
                            }
                        }

                        MouseArea {
                            anchors.fill: parent
                            onClicked: window.clickCount += 1
                        }
                    }
                }
            }
            """,
        },
    )

    write_day(
        3,
        "组件拆分和基础布局",
        "把重复 UI 拆成可复用 QML 组件，使用 Row 和 Column 组织界面。",
        ["单独的 QML 文件就是一个组件", "组件通过 property 暴露可配置内容", "Row/Column 适合简单线性布局"],
        "给 InfoCard 增加一个 footer 属性，并在三个卡片中显示不同内容。",
        "学习 Qt Quick Controls 控件。",
        {
            "CMakeLists.txt": cmake_for(3, qml_files=["Main.qml", "InfoCard.qml"]),
            "main.cpp": main_cpp(3),
            "InfoCard.qml": """
            import QtQuick

            Rectangle {
                id: root
                property string heading: "标题"
                property string body: "说明"
                property color accent: "#2563eb"

                width: 220
                height: 150
                radius: 12
                color: "white"
                border.color: "#dbe3ef"

                Column {
                    anchors.fill: parent
                    anchors.margins: 18
                    spacing: 10

                    Rectangle {
                        width: 38
                        height: 5
                        radius: 3
                        color: root.accent
                    }

                    Text {
                        text: root.heading
                        font.pixelSize: 20
                        font.bold: true
                        color: "#0f172a"
                    }

                    Text {
                        width: parent.width
                        text: root.body
                        wrapMode: Text.WordWrap
                        color: "#475569"
                    }
                }
            }
            """,
            "Main.qml": """
            import QtQuick

            Window {
                width: 820
                height: 480
                visible: true
                title: "Day 03 - Components"

                Rectangle {
                    anchors.fill: parent
                    color: "#f8fafc"

                    Column {
                        anchors.centerIn: parent
                        spacing: 24

                        Text {
                            text: "把界面拆成组件"
                            font.pixelSize: 32
                            font.bold: true
                            color: "#0f172a"
                        }

                        Row {
                            spacing: 18
                            InfoCard { heading: "QML"; body: "描述界面结构"; accent: "#2563eb" }
                            InfoCard { heading: "C++"; body: "承载数据和规则"; accent: "#16a34a" }
                            InfoCard { heading: "CMake"; body: "组织项目构建"; accent: "#ea580c" }
                        }
                    }
                }
            }
            """,
        },
    )

    write_day(
        4,
        "Qt Quick Controls",
        "使用 Button、TextField、Slider、Switch 等现成控件构建表单界面。",
        ["Controls 提供常用交互控件", "Layouts 负责自适应排版", "控件属性也可以参与绑定"],
        "增加一个 ComboBox，用来选择学习状态，并把选择结果显示在底部。",
        "学习状态和动画。",
        {
            "CMakeLists.txt": cmake_for(4),
            "main.cpp": main_cpp(4),
            "Main.qml": """
            import QtQuick
            import QtQuick.Controls
            import QtQuick.Layouts

            ApplicationWindow {
                width: 760
                height: 520
                visible: true
                title: "Day 04 - Controls"

                header: ToolBar {
                    Label {
                        anchors.centerIn: parent
                        text: "Qt Quick Controls 表单"
                        font.bold: true
                    }
                }

                ColumnLayout {
                    anchors.centerIn: parent
                    width: 420
                    spacing: 14

                    TextField {
                        id: nameField
                        Layout.fillWidth: true
                        placeholderText: "输入你的名字"
                    }

                    Slider {
                        id: progress
                        Layout.fillWidth: true
                        from: 0
                        to: 100
                        value: 30
                    }

                    Switch {
                        id: dailySwitch
                        text: "今天已经学习 QML"
                        checked: true
                    }

                    Button {
                        Layout.fillWidth: true
                        text: "生成学习摘要"
                        onClicked: result.text = (nameField.text || "学习者")
                            + "，当前进度 " + Math.round(progress.value)
                            + "%，今日状态：" + (dailySwitch.checked ? "已学习" : "未学习")
                    }

                    Label {
                        id: result
                        Layout.fillWidth: true
                        wrapMode: Text.WordWrap
                        text: "等待输入..."
                    }
                }
            }
            """,
        },
    )

    write_day(
        5,
        "状态和动画",
        "用 states 和 transitions 描述界面状态切换，并给变化添加动画。",
        ["State 表示一组属性变化", "Transition 描述状态之间的动画", "Behavior 适合给单个属性添加默认动画"],
        "把卡片展开后增加一段新的说明文字，并让透明度也参与动画。",
        "开始让 QML 调用 C++ 对象。",
        {
            "CMakeLists.txt": cmake_for(5),
            "main.cpp": main_cpp(5),
            "Main.qml": """
            import QtQuick

            Window {
                width: 780
                height: 520
                visible: true
                title: "Day 05 - States"

                Rectangle {
                    anchors.fill: parent
                    color: "#f8fafc"

                    Rectangle {
                        id: card
                        property bool expanded: false

                        width: 340
                        height: 180
                        radius: 18
                        anchors.centerIn: parent
                        color: "#dbeafe"

                        Column {
                            anchors.centerIn: parent
                            spacing: 10

                            Text {
                                text: card.expanded ? "展开状态" : "普通状态"
                                font.pixelSize: 30
                                font.bold: true
                                color: "#0f172a"
                            }

                            Text {
                                text: "点击卡片切换状态"
                                font.pixelSize: 17
                                color: "#475569"
                            }
                        }

                        MouseArea {
                            anchors.fill: parent
                            onClicked: card.expanded = !card.expanded
                        }

                        states: State {
                            name: "expanded"
                            when: card.expanded
                            PropertyChanges { target: card; width: 520; height: 300; color: "#dcfce7" }
                        }

                        transitions: Transition {
                            NumberAnimation { properties: "width,height"; duration: 260; easing.type: Easing.OutCubic }
                            ColorAnimation { duration: 260 }
                        }
                    }
                }
            }
            """,
        },
    )


def generate_cpp_intro_days() -> None:
    files6 = message_provider_files()
    files6.update({
        "CMakeLists.txt": cmake_for(6, sources=["MessageProvider.h", "MessageProvider.cpp"]),
        "main.cpp": main_cpp(
            6,
            includes='#include <QQmlContext>\n#include "MessageProvider.h"',
            before_engine="MessageProvider messageProvider;",
            after_engine='engine.rootContext()->setContextProperty("messageProvider", &messageProvider);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 760
            height: 500
            visible: true
            title: "Day 06 - QML calls C++"

            ColumnLayout {
                anchors.centerIn: parent
                width: 420
                spacing: 14

                Label { text: messageProvider.todayTopic(); font.pixelSize: 18 }
                TextField { id: nameField; Layout.fillWidth: true; placeholderText: "输入名字" }
                Button {
                    Layout.fillWidth: true
                    text: "调用 C++ greeting()"
                    onClicked: output.text = messageProvider.greeting(nameField.text)
                }
                Label {
                    id: output
                    Layout.fillWidth: true
                    text: "等待调用..."
                    wrapMode: Text.WordWrap
                    font.pixelSize: 20
                }
            }
        }
        """,
    })
    write_day(6, "QML 调用 C++ 方法", "用 context property 把 C++ 对象交给 QML，并从按钮点击里调用 Q_INVOKABLE 方法。", ["Q_INVOKABLE 让普通 C++ 方法能被 QML 调用", "QQmlContext 可以注入对象", "QML 不应该直接负责复杂业务规则"], "给 MessageProvider 增加一个 version() 方法，并在 QML 里显示。", "学习 Q_PROPERTY。", files6)

    files7 = counter_files()
    files7.update({
        "CMakeLists.txt": cmake_for(7, sources=["Counter.h", "Counter.cpp"]),
        "main.cpp": main_cpp(
            7,
            includes='#include <QQmlContext>\n#include "Counter.h"',
            before_engine="Counter counter;",
            after_engine='engine.rootContext()->setContextProperty("counter", &counter);',
        ),
        "Main.qml": """
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
        """,
    })
    write_day(7, "Q_PROPERTY 和属性通知", "把 C++ 属性暴露给 QML，并用 NOTIFY 信号驱动界面自动刷新。", ["Q_PROPERTY 定义 QML 可见属性", "READ/WRITE 指向 C++ getter/setter", "NOTIFY 信号让绑定知道何时刷新"], "给 Counter 增加 maxValue 属性，让 QML 的进度条上限来自 C++。", "学习 C++ 信号连接到 QML。", files7)

    files8 = notifier_files()
    files8.update({
        "CMakeLists.txt": cmake_for(8, sources=["Notifier.h", "Notifier.cpp"]),
        "main.cpp": main_cpp(
            8,
            includes='#include <QQmlContext>\n#include "Notifier.h"',
            before_engine="Notifier notifier;",
            after_engine='engine.rootContext()->setContextProperty("notifier", &notifier);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 760
            height: 520
            visible: true
            title: "Day 08 - Signals"

            ColumnLayout {
                anchors.centerIn: parent
                width: 480
                spacing: 12

                TextField { id: input; Layout.fillWidth: true; placeholderText: "通知内容" }
                Button { Layout.fillWidth: true; text: "让 C++ 发信号"; onClicked: notifier.sendNotice(input.text) }
                TextArea {
                    id: logText
                    Layout.fillWidth: true
                    Layout.preferredHeight: 220
                    readOnly: true
                    text: "通知日志\\n"
                }
            }

            Connections {
                target: notifier
                function onNotice(message) {
                    logText.text = message + "\\n" + logText.text
                }
            }
        }
        """,
    })
    write_day(8, "C++ 信号传到 QML", "从 C++ 发出信号，在 QML 里用 Connections 响应。", ["signals 定义 C++ 发出的事件", "Connections 可以监听 context property 的信号", "信号适合表达状态变化和异步结果"], "让 sendNotice() 同时传出当前时间，并在 QML 日志里显示。", "学习带参数的 C++ 方法和简单计算。", files8)

    files9 = calculator_files()
    files9.update({
        "CMakeLists.txt": cmake_for(9, sources=["Calculator.h", "Calculator.cpp"]),
        "main.cpp": main_cpp(
            9,
            includes='#include <QQmlContext>\n#include "Calculator.h"',
            before_engine="Calculator calculator;",
            after_engine='engine.rootContext()->setContextProperty("calculator", &calculator);',
        ),
        "Main.qml": """
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
        """,
    })
    write_day(9, "QML 传参给 C++", "从 QML 把数字和操作符传给 C++，由 C++ 返回计算结果。", ["QML 的 Number 可以转换输入框文本", "Q_INVOKABLE 支持带参数和返回值", "C++ 方法要处理非法输入或边界条件"], "给 Calculator 增加平方运算，并在 ComboBox 里加入对应选项。", "学习 QVariant、QStringList 和列表数据。", files9)

    files10 = data_bridge_files()
    files10.update({
        "CMakeLists.txt": cmake_for(10, sources=["DataBridge.h", "DataBridge.cpp"]),
        "main.cpp": main_cpp(
            10,
            includes='#include <QQmlContext>\n#include "DataBridge.h"',
            before_engine="DataBridge bridge;",
            after_engine='engine.rootContext()->setContextProperty("bridge", &bridge);',
        ),
        "Main.qml": """
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
        """,
    })
    write_day(10, "QVariant 数据交换", "用 QStringList 和 QVariantList 在 C++ 与 QML 之间传递简单列表数据。", ["QStringList 可以直接作为 QML model", "QVariantMap 字段可在 QML 中通过点号访问", "复杂列表后面应使用 QAbstractListModel"], "给 tasks() 多加一个字段，比如 estimate，并在 QML 里显示。", "学习 QStringListModel。", files10)


def generate_model_days() -> None:
    write_day(
        11,
        "QStringListModel 入门",
        "用 Qt 自带模型把 C++ 字符串列表交给 QML ListView。",
        ["QStringListModel 适合简单字符串列表", "ListView 根据 model 生成 delegate", "display 是 QStringListModel 的默认角色"],
        "在 main.cpp 里多加入两个主题，观察 ListView 自动显示。",
        "学习自定义 QAbstractListModel。",
        {
            "CMakeLists.txt": cmake_for(11),
            "main.cpp": main_cpp(
                11,
                includes="#include <QQmlContext>\n#include <QStringListModel>",
                before_engine='QStringListModel topicModel(QStringList{QStringLiteral("QML 绑定"), QStringLiteral("C++ 对象"), QStringLiteral("模型视图"), QStringLiteral("JSON 保存")});',
                after_engine='engine.rootContext()->setContextProperty("topicModel", &topicModel);',
            ),
            "Main.qml": """
            import QtQuick
            import QtQuick.Controls
            import QtQuick.Layouts

            ApplicationWindow {
                width: 760
                height: 520
                visible: true
                title: "Day 11 - QStringListModel"

                ListView {
                    anchors.fill: parent
                    anchors.margins: 24
                    spacing: 8
                    model: topicModel
                    delegate: Rectangle {
                        width: ListView.view.width
                        height: 54
                        radius: 10
                        color: "#f8fafc"
                        border.color: "#dbe3ef"
                        Text {
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            anchors.leftMargin: 16
                            text: model.display
                            font.pixelSize: 18
                        }
                    }
                }
            }
            """,
        },
    )

    files12 = simple_task_model_files()
    files12.update({
        "CMakeLists.txt": cmake_for(12, sources=["TaskListModel.h", "TaskListModel.cpp"]),
        "main.cpp": main_cpp(
            12,
            includes='#include <QQmlContext>\n#include "TaskListModel.h"',
            before_engine="TaskListModel taskModel;",
            after_engine='engine.rootContext()->setContextProperty("taskModel", &taskModel);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 820
            height: 560
            visible: true
            title: "Day 12 - QAbstractListModel"

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 24
                spacing: 12

                RowLayout {
                    Layout.fillWidth: true
                    TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "新任务标题" }
                    Button { text: "添加"; onClicked: { taskModel.addTask(titleInput.text); titleInput.clear() } }
                }

                ListView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: taskModel
                    spacing: 8
                    delegate: ItemDelegate {
                        width: ListView.view.width
                        text: (done ? "✓ " : "□ ") + title
                        onClicked: taskModel.toggleDone(index)
                    }
                }
            }
        }
        """,
    })
    write_day(12, "自定义 QAbstractListModel", "实现自己的 C++ 列表模型，为 QML 提供 title 和 done 两个角色。", ["rowCount 返回行数", "data 根据 role 返回字段", "roleNames 定义 QML 可见字段名", "beginInsertRows/endInsertRows 通知视图插入数据"], "增加一个 PriorityRole，并在 QML delegate 中显示优先级。", "进一步把 C++ 模型绑定到更完整的列表界面。", files12)

    files13 = simple_task_model_files("TaskListModel")
    files13.update({
        "CMakeLists.txt": cmake_for(13, sources=["TaskListModel.h", "TaskListModel.cpp"]),
        "main.cpp": main_cpp(
            13,
            includes='#include <QQmlContext>\n#include "TaskListModel.h"',
            before_engine="TaskListModel taskModel;",
            after_engine='engine.rootContext()->setContextProperty("taskModel", &taskModel);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 860
            height: 580
            visible: true
            title: "Day 13 - Model + Delegate"

            SplitView {
                anchors.fill: parent

                ListView {
                    id: list
                    SplitView.preferredWidth: 360
                    model: taskModel
                    clip: true
                    delegate: ItemDelegate {
                        width: list.width
                        text: title
                        highlighted: ListView.isCurrentItem
                        onClicked: list.currentIndex = index
                    }
                }

                Frame {
                    SplitView.fillWidth: true
                    ColumnLayout {
                        anchors.fill: parent
                        anchors.margins: 16
                        Label { text: list.currentIndex >= 0 ? taskModel.get ? "选择了任务" : "当前任务" : "请选择任务"; font.pixelSize: 22 }
                        Label { text: "点击左侧列表项，后续 App 会在这里展示详情页。"; wrapMode: Text.WordWrap }
                        Button { text: "删除当前行"; enabled: list.currentIndex >= 0; onClicked: taskModel.removeTask(list.currentIndex) }
                    }
                }
            }
        }
        """,
    })
    write_day(13, "ListView delegate 和详情区", "让列表和详情区协同工作，为后半段完整 App 做界面准备。", ["SplitView 可以做左右分栏", "ListView.currentIndex 表示当前选择", "delegate 负责单条数据的显示和点击"], "把右侧详情区改成显示当前任务标题和完成状态。", "学习 JSON 文件读写。", files13)

    files14 = json_store_files()
    files14.update({
        "CMakeLists.txt": cmake_for(14, sources=["JsonStore.h", "JsonStore.cpp"]),
        "main.cpp": main_cpp(
            14,
            includes='#include <QQmlContext>\n#include "JsonStore.h"',
            before_engine="JsonStore store;",
            after_engine='engine.rootContext()->setContextProperty("store", &store);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 820
            height: 560
            visible: true
            title: "Day 14 - JSON Store"

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 24
                spacing: 12

                RowLayout {
                    Layout.fillWidth: true
                    TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "输入一条本地数据" }
                    Button { text: "添加并保存"; onClicked: { store.addItem(titleInput.text); titleInput.clear() } }
                    Button { text: "重新加载"; onClicked: store.load() }
                }

                ListView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: store.items
                    delegate: ItemDelegate {
                        width: ListView.view.width
                        text: modelData.title
                    }
                }
            }
        }
        """,
    })
    write_day(14, "JSON 本地保存", "用 QJsonDocument 把 C++ 数据保存到应用数据目录，并再次加载。", ["QStandardPaths 能找到跨平台应用数据目录", "QJsonArray/QJsonObject 适合保存结构化数据", "保存失败要返回 bool 让 QML 能提示用户"], "给每条数据增加 createdAt 字段，并在 QML 列表中显示。", "做一个小综合任务列表。", files14)

    files15 = task_store_files()
    files15.update({
        "CMakeLists.txt": cmake_for(15, sources=["TaskStore.h", "TaskStore.cpp"]),
        "main.cpp": main_cpp(
            15,
            includes='#include <QQmlContext>\n#include "TaskStore.h"',
            before_engine="TaskStore taskStore;",
            after_engine='engine.rootContext()->setContextProperty("taskStore", &taskStore);',
        ),
        "Main.qml": """
        import QtQuick
        import QtQuick.Controls
        import QtQuick.Layouts

        ApplicationWindow {
            width: 860
            height: 600
            visible: true
            title: "Day 15 - Mini Task App"

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 24
                spacing: 12

                Label { text: "小综合：本地任务列表"; font.pixelSize: 24; font.bold: true }

                RowLayout {
                    Layout.fillWidth: true
                    TextField { id: titleInput; Layout.fillWidth: true; placeholderText: "任务标题" }
                    Button { text: "添加"; onClicked: { taskStore.addTask(titleInput.text); titleInput.clear() } }
                }

                ListView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: taskStore.tasks
                    spacing: 8
                    delegate: ItemDelegate {
                        width: ListView.view.width
                        text: (modelData.done ? "✓ " : "□ ") + modelData.title
                        onClicked: taskStore.toggleTask(index)
                        Button {
                            anchors.right: parent.right
                            anchors.verticalCenter: parent.verticalCenter
                            text: "删除"
                            onClicked: taskStore.removeTask(index)
                        }
                    }
                }
            }
        }
        """,
    })
    write_day(15, "小综合：本地任务列表", "把 QML 控件、C++ 数据对象和 JSON 保存合在一起，完成一个小型本地任务列表。", ["QML 负责输入和列表展示", "C++ 负责增删改和保存", "QVariantList 适合小练习，大项目应切换到模型"], "把任务列表增加一个清空已完成按钮。", "进入 15 天完整任务/笔记管理 App。", files15)


def generate_app_days() -> None:
    write_day(
        16,
        "完整 App：界面框架",
        "先搭出任务/笔记管理 App 的窗口、顶部栏、左右分栏和详情区。",
        ["ApplicationWindow 适合完整应用", "SplitView 可以做主从布局", "先定界面骨架，再接入数据模型"],
        "把左侧导航改成三项：全部、今日、归档。",
        "加入 C++ TaskModel。",
        {
            "CMakeLists.txt": cmake_for(16),
            "main.cpp": main_cpp(16),
            "Main.qml": """
            import QtQuick
            import QtQuick.Controls
            import QtQuick.Layouts

            ApplicationWindow {
                width: 1040
                height: 680
                visible: true
                title: "Day 16 - App Shell"

                header: ToolBar {
                    Label {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 12
                        text: "任务 / 笔记管理"
                        font.bold: true
                        font.pixelSize: 18
                    }
                }

                SplitView {
                    anchors.fill: parent
                    Frame {
                        SplitView.preferredWidth: 280
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "导航"; font.bold: true }
                            Button { Layout.fillWidth: true; text: "全部任务" }
                            Button { Layout.fillWidth: true; text: "笔记" }
                            Button { Layout.fillWidth: true; text: "设置" }
                        }
                    }
                    Frame {
                        SplitView.fillWidth: true
                        ColumnLayout {
                            anchors.centerIn: parent
                            Label { text: "详情区"; font.pixelSize: 28; font.bold: true }
                            Label { text: "后续每天会在这个框架中加入数据模型和功能。" }
                        }
                    }
                }
            }
            """,
        },
    )

    app_day_titles = {
        17: "完整 App：任务模型",
        18: "完整 App：新增任务",
        19: "完整 App：删除任务",
        20: "完整 App：编辑任务",
        21: "完整 App：完成状态",
        22: "完整 App：搜索筛选",
        23: "完整 App：分类标签",
        24: "完整 App：笔记详情",
        25: "完整 App：JSON 持久化",
        26: "完整 App：空状态和错误反馈",
        27: "完整 App：界面优化",
        28: "完整 App：导入导出",
        29: "完整 App：部署准备",
        30: "完整 App：复盘和扩展",
    }
    goals = {
        17: "用 C++ QAbstractListModel 作为完整 App 的数据核心。",
        18: "在 QML 表单中收集输入，并调用 C++ 模型新增任务。",
        19: "通过当前选择行删除 C++ 模型中的任务。",
        20: "把详情区变成可编辑表单，并把修改写回模型。",
        21: "增加完成/未完成状态，理解 dataChanged 的作用。",
        22: "加入搜索框，让 C++ 模型根据关键字重建可见列表。",
        23: "加入分类字段，并按分类筛选任务。",
        24: "把任务的 note 字段作为笔记详情维护。",
        25: "把任务保存到 JSON 文件，并在启动时加载。",
        26: "为空列表和失败操作增加清晰反馈。",
        27: "优化状态栏和计数信息，让 App 更像完整工具。",
        28: "支持导出和导入 JSON 文件，练习文件路径处理。",
        29: "理解 windeployqt 和发布前检查项。",
        30: "复盘 QML + C++ 混合开发路径，并保留可扩展最终版本。",
    }
    exercises = {
        17: "给 TaskModel 增加一个新的默认任务，重新构建后观察列表。",
        18: "给新增表单加一个默认分类，并传给 C++。",
        19: "删除任务后清空详情区，避免显示旧数据。",
        20: "编辑任务后自动调用 save()，让修改立刻落盘。",
        21: "把已完成任务显示成灰色或加删除线。",
        22: "让搜索同时匹配分类字段。",
        23: "增加一个新的分类选项，并作为默认新增分类。",
        24: "给 note 增加字数统计。",
        25: "在状态栏里显示保存成功或失败。",
        26: "给导入失败、保存失败分别显示不同提示。",
        27: "调整窗口尺寸和 SplitView 宽度，让阅读更舒服。",
        28: "把导出文件名改成带日期的文件名。",
        29: "试着运行 windeployqt 打包 day30 的可执行文件。",
        30: "选择一个扩展方向：数据库、网络同步、提醒通知，写下你会新增哪些 C++ 类。",
    }

    for day in range(17, 31):
        files = task_model_final_files()
        files.update({
            "CMakeLists.txt": cmake_for(day, sources=["TaskModel.h", "TaskModel.cpp"]),
            "main.cpp": main_cpp(
                day,
                includes='#include <QQmlContext>\n#include "TaskModel.h"',
                before_engine="TaskModel taskModel;",
                after_engine='engine.rootContext()->setContextProperty("taskModel", &taskModel);',
            ),
            "Main.qml": final_app_qml(day, app_day_titles[day]),
        })
        write_day(
            day,
            app_day_titles[day],
            goals[day],
            ["QML 继续负责界面和交互", "C++ TaskModel 负责数据、筛选、保存和导入导出", "每天在同一个 App 思路上增加一个可观察能力"],
            exercises[day],
            "继续完善任务/笔记管理 App。" if day < 30 else "课程结束后可以扩展为数据库版或网络同步版。",
            files,
        )


def write_shared_files() -> None:
    write_file(
        "assets/style.css",
        """
        :root {
          color-scheme: light;
          font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
          background: #f6f8fb;
          color: #172033;
        }

        body {
          margin: 0;
          background: #f6f8fb;
        }

        .page {
          width: min(980px, calc(100vw - 32px));
          margin: 0 auto;
          padding: 28px 0 56px;
        }

        .topline {
          display: flex;
          justify-content: space-between;
          gap: 12px;
          margin-bottom: 22px;
          color: #64748b;
        }

        a {
          color: #0f5cc0;
          text-decoration: none;
        }

        a:hover {
          text-decoration: underline;
        }

        h1 {
          margin: 0 0 22px;
          font-size: 34px;
          line-height: 1.2;
        }

        h2 {
          margin: 28px 0 10px;
          font-size: 22px;
        }

        p, li {
          line-height: 1.75;
          font-size: 16px;
        }

        code {
          font-family: Consolas, "Cascadia Code", monospace;
          background: #eef2f7;
          padding: 2px 5px;
          border-radius: 4px;
        }

        pre {
          overflow: auto;
          background: #101827;
          color: #dbeafe;
          padding: 16px;
          border-radius: 8px;
        }

        pre code {
          background: transparent;
          padding: 0;
        }

        .panel, section {
          background: #ffffff;
          border: 1px solid #dbe3ef;
          border-radius: 8px;
          padding: 18px 22px;
          margin: 14px 0;
        }

        .grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
          gap: 12px;
        }

        .day-card {
          background: #ffffff;
          border: 1px solid #dbe3ef;
          border-radius: 8px;
          padding: 16px;
        }

        .day-card h2 {
          margin-top: 0;
          font-size: 18px;
        }

        .next {
          border-color: #bfdbfe;
          background: #eff6ff;
        }
        """,
    )

    cards = "\n".join(
        f"""
        <article class="day-card">
          <h2>第 {item['day']} 天</h2>
          <p><a href="day{item['day']}/docs.html">{html.escape(item['title'])}</a></p>
          <p>{html.escape(item['goal'])}</p>
        </article>
        """
        for item in days_meta
    )

    write_file(
        "index.html",
        f"""
        <!doctype html>
        <html lang="zh-CN">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>30 天学习 QML + C++</title>
          <link rel="stylesheet" href="assets/style.css">
        </head>
        <body>
          <main class="page">
            <h1>30 天学习 QML + C++</h1>
            <section class="panel">
              <p>这套教程按 Qt 6.11.1、CMake、MinGW 环境编写。前 15 天是独立练习，后 15 天持续完善一个任务/笔记管理 App。</p>
              <p>每一天都有可运行代码、<code>run.ps1</code> 和 HTML 讲义。建议按顺序学习，但每个目录都可以独立构建。</p>
            </section>
            <div class="grid">
              {cards}
            </div>
          </main>
        </body>
        </html>
        """,
    )

    write_file(
        "README.md",
        f"""
        # 30 天学习 QML + C++

        这是为本机 Qt 6.11.1 + MinGW 环境生成的 30 天教程。

        ## 打开讲义

        用浏览器打开：

        ```powershell
        .\\qml-cpp-30days\\index.html
        ```

        ## 构建某一天

        例如第 1 天：

        ```powershell
        cd qml-cpp-30days\\day01
        .\\run.ps1
        ```

        如果只想构建不运行：

        ```powershell
        cmake -S . -B build -G Ninja -DCMAKE_PREFIX_PATH={QT_PREFIX} -DCMAKE_MAKE_PROGRAM={NINJA} -DCMAKE_CXX_COMPILER={CXX}
        cmake --build build
        ```

        ## 学习顺序

        - day01-day15：QML 基础、C++ 对象、属性、信号、模型、JSON。
        - day16-day30：逐步完成任务/笔记管理 App。

        ## 常见问题

        如果直接运行 exe 提示缺少 Qt DLL，请先在当前 PowerShell 加入 Qt 路径：

        ```powershell
        $env:Path = "C:\\Qt\\6.11.1\\mingw_64\\bin;C:\\Qt\\Tools\\mingw1310_64\\bin;" + $env:Path
        ```
        """,
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    generate_basic_days()
    generate_cpp_intro_days()
    generate_model_days()
    generate_app_days()
    write_shared_files()
    print(f"Generated tutorial at {OUT}")


if __name__ == "__main__":
    main()
