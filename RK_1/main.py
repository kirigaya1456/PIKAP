from datetime import date


class Database:
    def __init__(self, database_id, name, engine, size_mb):
        self.database_id = database_id
        self.name = name
        self.engine = engine                # Пример: "PostgreSQL"
        self.size_mb = size_mb              # Размер в МБ


class StoredProcedure:
    def __init__(self, procedure_id, name, language, author, last_modified_date, database_id, execution_count):
        self.procedure_id = procedure_id
        self.name = name
        self.language = language            # Пример: "PL/pgSQL"
        self.author = author                # Автор процедуры
        self.last_modified_date = last_modified_date  # Последнее изменение (date)
        self.database_id = database_id
        self.execution_count = execution_count  # Количество запусков


class ProcedureDatabaseLink:
    def __init__(self, procedure_id, database_id):
        self.procedure_id = procedure_id
        self.database_id = database_id


# Тестовые данные
databases = [
    Database(1, "AlphaDB", "PostgreSQL", 1024),
    Database(2, "BetaDB", "MySQL", 2048),
    Database(3, "Artemis", "Oracle", 800),
    Database(4, "Omega", "SQLite", 350)
]

procedures = [
    StoredProcedure(1, "process_sales", "PL/pgSQL",
                    "Ivanov", date(2025, 10, 1), 1, 55),
    StoredProcedure(2, "clean_orders", "PL/pgSQL",
                    "Sidorov", date(2025, 9, 5), 1, 120),
    StoredProcedure(3, "archive_data", "T-SQL",
                    "Petrov", date(2025, 8, 30), 2, 34),
    StoredProcedure(4, "check_integrity", "PL/SQL",
                    "Orlova", date(2025, 6, 7), 3, 12),
    StoredProcedure(5, "send_reports", "Python",
                    "Kim", date(2025, 10, 25), 3, 66)
]

links = [
    ProcedureDatabaseLink(1, 1),
    ProcedureDatabaseLink(2, 1),
    ProcedureDatabaseLink(3, 2),
    ProcedureDatabaseLink(4, 3),
    ProcedureDatabaseLink(5, 3),
    ProcedureDatabaseLink(5, 2)  # Для many-to-many
]


def main():
    # Запрос 1: базы данных на "А" и их процедуры
    print("Request 1:")
    databases_starting_with_a = [db for db in databases if db.name.startswith('A')]
    result_1 = [
        {
            'database_name': db.name,
            'procedures': [procedure.name for procedure in procedures
                          if procedure.database_id == db.database_id]
        }
        for db in databases_starting_with_a
    ]
    for row in result_1:
        print(f"Database: {row['database_name']} | Procedures: {', '.join(row['procedures'])}")
    print()

    # Запрос 2: максимальное количество запусков процедур по базам, по убыванию
    print("Request 2:")
    database_max_executions = []
    for database in databases:
        database_procedures = [procedure for procedure in procedures
                              if procedure.database_id == database.database_id]
        if database_procedures:
            max_execution_count = max(procedure.execution_count
                                     for procedure in database_procedures)
            database_max_executions.append(
                {'database_name': database.name, 'max_execution_count': max_execution_count})

    database_max_executions.sort(key=lambda x: x['max_execution_count'], reverse=True)
    for row in database_max_executions:
        print(f"Database: {row['database_name']} | Max Execution Count: {row['max_execution_count']}")
    print()

    # Запрос 3: many-to-many - процедуры и базы, отсортировано по базе
    print("Request 3:")
    database_dict = {database.database_id: database.name for database in databases}
    procedure_dict = {procedure.procedure_id: procedure.name for procedure in procedures}

    many_to_many_relations = [
        (database_dict[link.database_id], procedure_dict[link.procedure_id])
        for link in links
    ]
    many_to_many_relations.sort(key=lambda x: (x[0], x[1]))

    for database_name, procedure_name in many_to_many_relations:
        print(f"Database: {database_name} | Procedure: {procedure_name}")
    print()


if __name__ == '__main__':
    main()
