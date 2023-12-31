"""relpart2

Revision ID: e989dc0a4660
Revises: 
Create Date: 2023-08-07 12:38:37.279270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e989dc0a4660'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books'))
    )
    op.create_table('days',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('weekday', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_days'))
    )
    op.create_table('bookratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_bookratings_book_id_books')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bookratings'))
    )
    op.create_table('dayratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('day_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['day_id'], ['days.id'], name=op.f('fk_dayratings_day_id_days')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_dayratings'))
    )
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('day_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_schedules_book_id_books')),
    sa.ForeignKeyConstraint(['day_id'], ['days.id'], name=op.f('fk_schedules_day_id_days')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_schedules'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedules')
    op.drop_table('dayratings')
    op.drop_table('bookratings')
    op.drop_table('days')
    op.drop_table('books')
    # ### end Alembic commands ###
