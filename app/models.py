# from sqlalchemy import TIMESTAMP, Boolean, ForeignKey, Integer, String, text
# from .database import engine
# from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

# class Base(DeclarativeBase):
#     pass


# class Post(Base):     
#     __tablename__ = "posts"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     content: Mapped[str]= mapped_column(String, nullable=False)
#     published: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default='TRUE')
#     created_at = mapped_column(TIMESTAMP, nullable=False, server_default=text('now()'))
#     user_id = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

#     owner = relationship("User")

# class User(Base):
#     __tablename__ = "users"
    
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
#     email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
#     password: Mapped[str] = mapped_column(String, nullable=False)
#     created_at = mapped_column(TIMESTAMP, nullable=False, server_default=text('now()'))

# class Vote(Base):
#     __tablename__ = "votes"
#     user_id = mapped_column(Integer, ForeignKey(
#         "users.id", ondelete="CASCADE"), primary_key=True)
#     post_id = mapped_column(Integer, ForeignKey(
#         "posts.id", ondelete="CASCADE"), primary_key=True)
    
# Base.metadata.create_all(engine)
