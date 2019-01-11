"""Adding UserSiteRankings model

Revision ID: 4519159d3019
Revises: e3e42c7b6077
Create Date: 2018-12-29 19:46:37.660652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4519159d3019'
down_revision = 'e3e42c7b6077'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_site_rankings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comp_id', sa.Integer(), nullable=True),
    sa.Column('data', sa.String(length=2048), nullable=True),
    sa.ForeignKeyConstraint(['comp_id'], ['competitions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_site_rankings', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_site_rankings_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_site_rankings', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_site_rankings_user_id'))

    op.drop_table('user_site_rankings')
    # ### end Alembic commands ###