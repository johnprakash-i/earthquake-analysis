import os
import mysql.connector
from mysql.connector import Error
from config.db_config import get_connection

# Folder where all .sql migration files are stored
MIGRATIONS_DIR = "migrations"


def ensure_migration_table(conn):
    """
    Create a table (migrations_applied) if it does not exist.
    This table stores names of migration files that have already been executed.
    Helps prevent running the same migration twice.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS migrations_applied (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255),
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    )
    conn.commit()
    cursor.close()


def get_applied_migrations(conn):
    """
    Fetch all previously applied migration filenames from the database.
    Returns them as a Python set for fast lookup.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM migrations_applied;")
    rows = cursor.fetchall()
    cursor.close()

    return {row[0] for row in rows}  # Convert list of tuples → set of strings


def apply_migration(conn, filename, sql_content):
    """
    Execute the SQL commands from a single migration file.
    After successful execution, store the filename in migrations_applied table.
    """
    cursor = conn.cursor()
    print(f"📌 Applying migration: {filename}")

    # Split SQL content by semicolon to execute each statement safely
    statements = sql_content.split(";")

    for stmt in statements:
        stmt = stmt.strip()
        if stmt:  # Avoid running empty statements
            cursor.execute(stmt)

    # Record this migration as applied
    cursor.execute(
        "INSERT INTO migrations_applied (filename) VALUES (%s);", (filename,)
    )

    conn.commit()
    cursor.close()

    print(f"✔ Successfully applied: {filename}")


def run_migrations():
    """
    Main function to execute all pending migration files.

    Steps:
    1. Connect to DB
    2. Ensure tracking table exists
    3. Get list of already applied migrations
    4. Loop through migration folder
    5. Execute only the new migration files
    """
    conn = get_connection()
    ensure_migration_table(conn)

    applied = get_applied_migrations(conn)  # Set of already-run files

    # Read all migration files in sorted order (001, 002, 003…)
    migration_files = sorted(os.listdir(MIGRATIONS_DIR))

    for file in migration_files:
        # Skip non-SQL files (just in case)
        if not file.endswith(".sql"):
            continue

        # Skip if already applied earlier
        if file in applied:
            print(f"⏭ Skipping (already applied): {file}")
            continue

        # Full path to migration file
        path = os.path.join(MIGRATIONS_DIR, file)

        # Read the SQL content
        with open(path, "r") as f:
            sql = f.read()

        # Apply the migration
        apply_migration(conn, file, sql)

    conn.close()
    print("\n🎉 All migrations completed successfully!")


# Run the migration process when this file is executed directly
if __name__ == "__main__":
    run_migrations()
