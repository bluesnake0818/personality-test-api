"""empty message

Revision ID: 9c4963f8977d
Revises: 1ff5108b84db
Create Date: 2022-04-14 10:13:33.642228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4963f8977d'
down_revision = '1ff5108b84db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personalities', sa.Column('ans_1', sa.String(length=100), nullable=True))
    op.add_column('personalities', sa.Column('ans_2', sa.String(length=100), nullable=True))
    op.add_column('personalities', sa.Column('ans_3', sa.String(length=100), nullable=True))
    op.add_column('personalities', sa.Column('ans_4', sa.String(length=100), nullable=True))
    op.add_column('personalities', sa.Column('ans_5', sa.String(length=100), nullable=True))
    op.drop_column('personalities', 'answer_2')
    op.drop_column('personalities', 'answer_3')
    op.drop_column('personalities', 'answer_5')
    op.drop_column('personalities', 'answer_4')
    op.drop_column('personalities', 'answer_1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personalities', sa.Column('answer_1', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('personalities', sa.Column('answer_4', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('personalities', sa.Column('answer_5', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('personalities', sa.Column('answer_3', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('personalities', sa.Column('answer_2', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('personalities', 'ans_5')
    op.drop_column('personalities', 'ans_4')
    op.drop_column('personalities', 'ans_3')
    op.drop_column('personalities', 'ans_2')
    op.drop_column('personalities', 'ans_1')
    # ### end Alembic commands ###