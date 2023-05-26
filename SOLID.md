# SOLID

## 單一職責原則
一個類別只負責一項職責，且只有在一種理由下會變動。

> A class should have only on reason to change.

Animal有兩個獨立的功能，get_name和save，當動物名字或資料庫改變時都會影響Animal，故違反SRP。
```python
class Animal():
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        """show Animal name"""
        print(self.name)

    def save(self, animal: Animal):
        """save Animal to database"""
        pass

```

修正方法: 將save功能獨立成一個類別AnimalDB
```python
class Animal():
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        """show Animal name"""
        print(self.name)

    def get(self, id):
        return db.get_animal()

    def save(self):
        self.db.save(animal=self)

class AnimalDB():
    def get_animal(self, id) -> Animal:
        pass
    
    def save(self, animal: Animal):
        """save Animal to database"""
        pass
```


##