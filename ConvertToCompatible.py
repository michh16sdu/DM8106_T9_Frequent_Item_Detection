import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path

'''
Der er problemer med parquet tingen på grund af TIME kolonnen. Den er gemt som 32-bit integers. Det er vist problematisk for min spark version.

Hvis I render ind i det samme problem, så er der det her program til at konvertere det til en kompatibel parquet fil.

'''

def converter():
    source = Path(r"C:\Github\standard-chess-games-high-elo")
    destination = Path(r"C:\Github\chess-spark-compatible")
    destination.mkdir(exist_ok=True)

    for file in source.rglob("*.parquet"):
        table = pq.read_table(file)

        for name in table.column_names:
            column = table[name]

            if pa.types.is_time32(column.type) or pa.types.is_time64(column.type):
                index = table.schema.get_field_index(name)

                table = table.set_column(
                    index,
                    name,
                    column.cast(pa.string())
                )

        output = destination / file.relative_to(source)
        output.parent.mkdir(parents=True, exist_ok=True)

        pq.write_table(table, output)

    print("Done")
    return destination
    
