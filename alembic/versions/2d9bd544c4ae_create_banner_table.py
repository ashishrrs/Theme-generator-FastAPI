"""create banner table

Revision ID: 2d9bd544c4ae
Revises: 
Create Date: 2021-06-28 10:31:20.712872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d9bd544c4ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'banners',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('description', sa.String(200), nullable=False),
        sa.Column('url', sa.String(100), nullable=False),
        sa.Column('url_image', sa.String(200), nullable=False),
        sa.Column('published', sa.Boolean),
        sa.Column('is_widget', sa.Boolean),
        sa.Column('priority', sa.Integer, nullable=False),
    )


def downgrade():
    pass
