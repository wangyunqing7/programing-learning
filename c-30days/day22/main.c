#include <stdio.h>
#include <string.h>

/* 第 22 天：小型通讯录
 * 用结构体数组管理联系人。
 */
#define MAX_CONTACTS 100

typedef struct {
    char name[32];
    char phone[20];
} Contact;

typedef struct {
    Contact data[MAX_CONTACTS];
    int count;
} AddressBook;

void book_init(AddressBook *b) { b->count = 0; }

void book_add(AddressBook *b, const char *name, const char *phone) {
    if (b->count >= MAX_CONTACTS) { printf("通讯录已满\n"); return; }
    strcpy(b->data[b->count].name, name);
    strcpy(b->data[b->count].phone, phone);
    b->count++;
}

Contact* book_find(AddressBook *b, const char *name) {
    for (int i = 0; i < b->count; i++) {
        if (strcmp(b->data[i].name, name) == 0) return &b->data[i];
    }
    return NULL;
}

void book_print(AddressBook *b) {
    printf("通讯录（共 %d 人）：\n", b->count);
    for (int i = 0; i < b->count; i++) {
        printf("  %s  %s\n", b->data[i].name, b->data[i].phone);
    }
}

int main(void) {
    AddressBook book;
    book_init(&book);
    book_add(&book, "Ada", "138-0000-0001");
    book_add(&book, "Linus", "138-0000-0002");
    book_add(&book, "Grace", "138-0000-0003");
    book_print(&book);

    Contact *c = book_find(&book, "Linus");
    if (c) printf("\n找到：%s %s\n", c->name, c->phone);
    else   printf("\n没找到\n");
    return 0;
}