#include <stdio.h>
#include <string.h>

/* 第 28 天：迷你数据库
 * 用文件持久化的记录存储（文本格式）。
 */
#define MAX 50
typedef struct {
    int id;
    char name[24];
    int age;
} Record;

typedef struct {
    Record rows[MAX];
    int count;
} Database;

void db_add(Database *db, int id, const char *name, int age) {
    if (db->count < MAX) {
        db->rows[db->count++] = (Record){id, "", age};
        strcpy(db->rows[db->count-1].name, name);
    }
}

void db_save(Database *db, const char *path) {
    FILE *f = fopen(path, "w");
    for (int i = 0; i < db->count; i++)
        fprintf(f, "%d %s %d\n", db->rows[i].id, db->rows[i].name, db->rows[i].age);
    fclose(f);
}

void db_load(Database *db, const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return;
    db->count = 0;
    while (db->count < MAX &&
           fscanf(f, "%d %23s %d", &db->rows[db->count].id,
                  db->rows[db->count].name, &db->rows[db->count].age) == 3) {
        db->count++;
    }
    fclose(f);
}

void db_print(Database *db) {
    printf("数据库（%d 条）：\n", db->count);
    for (int i = 0; i < db->count; i++)
        printf("  #%d %s 年龄 %d\n", db->rows[i].id, db->rows[i].name, db->rows[i].age);
}

int main(void) {
    Database db = {0};
    db_add(&db, 1, "Ada", 36);
    db_add(&db, 2, "Linus", 54);
    db_add(&db, 3, "Grace", 85);
    db_print(&db);

    db_save(&db, "db.txt");
    printf("\n保存后重新加载：\n");
    Database db2 = {0};
    db_load(&db2, "db.txt");
    db_print(&db2);
    remove("db.txt");
    return 0;
}