<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
 #!/usr/bin/python3
 """Lists states"""
 
 from sqlalchemy import Column, Integer, String
 from sqlalchemy.orm import relationship
 from sqlalchemy.ext.declarative import declarative_base
+from .model_city import City
 
 Base = declarative_base()
 
 
 class State(Base):
     """Class representing the states table"""
     __tablename__ = 'states'
+    id = Column(Integer, primary_key=True,
                 autoincrement=True, unique=True)
+    name = Column(String(128), nullable=False)
<<<<<<<  8e2ca701-90ae-4a38-9998-ee785a6f9d4c  >>>>>>>