"""Initial migration

Revision ID: d92ac00c661a
Revises: 
Create Date: 2024-12-27 22:00:17.297034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd92ac00c661a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('creatures',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('aka', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('explorers',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('users',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('explorers')
    op.drop_table('creatures')
    # ### end Alembic commands ###
