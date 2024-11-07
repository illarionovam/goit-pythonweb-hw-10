from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas import ContactModel, UserResponse


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactModel, user: UserResponse):
        return await self.repository.create_contact(body, user)

    async def get_contacts(
        self,
        skip: int,
        limit: int,
        user: UserResponse,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
    ):
        return await self.repository.get_contacts(
            skip, limit, user, first_name, last_name, email
        )

    async def get_contacts_with_upcoming_birthdays(self, user: UserResponse):
        return await self.repository.get_contacts_with_upcoming_birthdays(user)

    async def get_contact(self, contact_id: int, user: UserResponse):
        return await self.repository.get_contact_by_id(contact_id, user)

    async def update_contact(
        self, contact_id: int, body: ContactModel, user: UserResponse
    ):
        return await self.repository.update_contact(contact_id, body, user)

    async def remove_contact(self, contact_id: int, user: UserResponse):
        return await self.repository.remove_contact(contact_id, user)
