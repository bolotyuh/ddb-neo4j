https://coderlessons.com/tutorials/bazy-dannykh/uznaite-neo4j/neo4j-kratkoe-rukovodstvo

### create node

```sql
CREATE (Node:Label{properties. . . . }) RETURN Node
```

### create relationship
```sql
CREATE (node1)-[:RelationshipType]->(node2)
```

### Создание связи между существующими узлами
```sql
MATCH (a:LabeofNode1), (b:LabeofNode2) 
    WHERE a.name = "nameofnode1" AND b.name = " nameofnode2" 
 CREATE (a)-[: Relation]->(b) 
 RETURN a,b 

```

### Создание отношений с меткой и свойствами
```sql
CREATE (node1)-[label:Rel_Type {key1:value1, key2:value2, . . . n}]-> (node2)


MATCH (a:player), (b:Country) WHERE a.name = "Shikar Dhawan" AND b.name = "India" 
CREATE (a)-[r:BATSMAN_OF {Matches:5, Avg:90.75}]->(b)  
RETURN a,b 
```

Команда MERGE является комбинацией команды CREATE и команды MATCH.
