"""empty message

Revision ID: 3682b6128ed6
Revises: a5cffa318ac2
Create Date: 2024-05-17 19:27:59.816628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3682b6128ed6'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('side', sa.String(length=30), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=True),
    sa.Column('origin', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('controled', sa.String(length=150), nullable=True),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('country', sa.String(length=60), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=80),
               nullable=True)
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('password')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('country')
        batch_op.drop_column('age')
        batch_op.drop_column('lastname')
        batch_op.drop_column('name')
        batch_op.drop_column('username')

    op.drop_table('favorite')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
