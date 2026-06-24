# QML + C++ 30-Day Tutorial Design

## Goal

Create a 30-day Chinese tutorial for learning QML with C++ integration on the local Qt 6.11.1 MinGW environment. Each day must include runnable Qt code and an HTML explanation document.

## Audience

The learner wants to start directly with QML + C++ mixed development. The course should still introduce QML fundamentals, but it should connect concepts to C++ objects, properties, signals, models, and local persistence as early as possible.

## Course Shape

Use a 15 + 15 structure.

Days 1-15 are independent focused exercises:

- QML project structure
- QML properties, binding, events, layout, controls, states, and animation
- QML calling C++
- `Q_PROPERTY`
- signals and slots
- QVariant-based data exchange
- QStringListModel
- `QAbstractListModel`
- JSON persistence
- a small local data-list exercise

Days 16-30 build a task and note management app in daily snapshots:

- app shell
- task model
- add, delete, edit, complete
- filtering and search
- category/tag fields
- detail page
- JSON save/load
- empty/error states
- interface polish
- import/export
- packaging notes
- final review and expansion paths

## Output Structure

Generate this structure under the current workspace:

```text
qml-cpp-30days/
  README.md
  index.html
  assets/style.css
  day01/
    CMakeLists.txt
    main.cpp
    Main.qml
    run.ps1
    docs.html
  ...
  day30/
    CMakeLists.txt
    main.cpp
    TaskModel.h
    TaskModel.cpp
    Main.qml
    run.ps1
    docs.html
```

Each `docs.html` explains:

- learning goal
- concepts
- code walkthrough
- build/run command
- common mistakes
- exercise
- tomorrow preview

## Technical Decisions

- Use Qt 6.11.1, CMake, Ninja, and MinGW 13.1.0.
- Use `qt_add_qml_module` so each daily app has a clean QML module.
- Keep every day runnable as an independent project.
- Use JSON files rather than a database so persistence stays focused on Qt and C++ basics.
- Avoid network services and external dependencies.

## Verification

After generation, configure and build representative days:

- Day 01: basic QML app
- Day 07: `Q_PROPERTY`
- Day 12: custom `QAbstractListModel`
- Day 14: JSON persistence
- Day 30: final task/note app

The final response must report any build failures honestly.
