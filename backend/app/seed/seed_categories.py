from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.subcategory import SubCategory

CATEGORY_DATA = {
    "Electronics": ["TVs", "Phones", "Laptops"],
    "Groceries": ["Dairy", "Fruits & Vegetables", "Snacks", "Beverages"],
    "Sport": ["Football (NFL)", "Basketball", "Baseball"],
    "Fashion": ["Jeans", "Shirts", "Shoes"],
}


def seed_categories(db: Session) -> None:
    for category_name, subcategories in CATEGORY_DATA.items():

        category = (
            db.query(Category)
            .filter(Category.name == category_name)
            .one_or_none()
        )

        if not category:
            category = Category(name=category_name)
            db.add(category)
            db.flush()  # ensures category.id is available

        for sub_name in subcategories:
            exists = (
                db.query(SubCategory)
                .filter(
                    SubCategory.name == sub_name,
                    SubCategory.category_id == category.id,
                )
                .one_or_none()
            )

            if not exists:
                db.add(
                    SubCategory(
                        name=sub_name,
                        category_id=category.id
                    )
                )

    db.commit()
