import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT count(distinct name) as total_num_chars FROM charactercreator_character;"
result = cursor.execute(query).fetchall
print("RESULT", result) 

query2 = "SELECT count(distinct character_ptr_id) as clerics FROM charactercreator_cleric;"
result2 = cursor.execute(query2).fetchall()
print("RESULT 2", result2)

query3 = "SELECT count(distinct character_ptr_id) as fighters FROM charactercreator_fighter;"
result3 = cursor.execute(query3).fetchall()
print("RESULT 3", result3)

query4 = "SELECT count(distinct character_ptr_id) as mages FROM charactercreator_mage;" 
result4 = cursor.execute(query4).fetchall()
print("RESULT 4", result4)

query5 = "SELECT count(distinct mage_ptr_id) as necromancers FROM charactercreator_necromancer;"
result5 = cursor.execute(query5).fetchall()
print("RESULT 5", result5)

query6 = "SELECT count(distinct character_ptr_id) as thieves FROM charactercreator_thief;"
result6 = cursor.execute(query6).fetchall()
print("RESULT 6", result6)

query7 = "SELECT count(distinct armory_item.name) as TotalItems ,count(distinct armory_weapon.item_ptr_id) as TotalWeapons From armory_item ,armory_weapon;"
result7 = cursor.execute(query7).fetchall()
print("RESULT 7", result7)

query8 = "SELECT count(distinct armory_item.name) as TotalItems ,count(distinct armory_weapon.item_ptr_id) as TotalWeapons From armory_item ,armory_weapon;"
result8 = cursor.execute(query8).fetchall()
print("RESULT 8", result8)

query9 = "SELECT character_id ,count(item_id) as Items FROM charactercreator_character_inventory GROUP BY character_id ORDER BY character_id ASC LIMIT 20;"
result9 = cursor.execute(query9).fetchall()
print("RESULT 9", result9)

query10 = "SELECT c.character_id ,c.name as character_name ,count(distinct w.item_ptr_id) as weapon_count FROM charactercreator_character as c LEFT JOIN charactercreator_character_inventory as inv ON c.character_id = inv.character_id LEFT JOIN armory_weapon as w ON w.item_ptr_id = inv.item_id GROUP BY c.character_id LIMIT 20;"
result10 = cursor.execute(query10).fetchall()
print("RESULT 10", result10)

query11 = "SELECT AVG(item_counts.item_count) FROM ( SELECT CCI.character_id ,COUNT(*) as item_count FROM charactercreator_character_inventory as CCI GROUP BY CCI.character_id ) AS item_counts;"
result11 = cursor.execute(query11).fetchall()
print("RESULT 11", result11)

query12 = "SELECT avg(weapon_counts.weapon_count) FROM ( SELECT cci.character_id ,count(*) as weapon_count FROM charactercreator_character_inventory as cci LEFT OUTER JOIN armory_weapon as aw ON cci.item_id = aw.item_ptr_id WHERE aw.item_ptr_id IS NOT NULL GROUP BY cci.character_id ) AS weapon_counts;"
result12 = cursor.execute(query12).fetchall()
print("RESULT 12", result12)