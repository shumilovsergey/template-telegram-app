from django.db import models
from django.utils import timezone

class TelegramUsers(models.Model):
    tg_id = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-auth")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tg_id
    class Meta:
        ordering = ['-created']








# Basic User Information

# Telegram.WebApp.initDataUnsafe.user.id: The unique user ID.
# Telegram.WebApp.initDataUnsafe.user.first_name: The user's first name.
# Telegram.WebApp.initDataUnsafe.user.last_name: The user's last name (optional).
# Telegram.WebApp.initDataUnsafe.user.username: The user's Telegram username (optional).
# Telegram.WebApp.initDataUnsafe.user.language_code: The user's language code (e.g., "en", "ru").

# Chat Information (for bots launched in groups or channels)

# Telegram.WebApp.initDataUnsafe.chat: Contains information about the chat where the bot was launched (only available in group chats or channels).
# Telegram.WebApp.initDataUnsafe.chat.id: The chat ID.
# Telegram.WebApp.initDataUnsafe.chat.type: The type of chat (group, supergroup, channel, etc.).
# Telegram.WebApp.initDataUnsafe.chat.title: The title of the chat.

# Environment Information

# Telegram.WebApp.platform: The platform on which the Web App is running (e.g., "ios", "android", "web").
# Telegram.WebApp.themeParams: An object containing the theme settings for the Telegram app, such as background color, button color, etc.
# Telegram.WebApp.colorScheme: Indicates whether the user is using "light" or "dark" mode.
# Telegram.WebApp.version: The version of Telegram that is being used.

# Other User Data

# Telegram.WebApp.initDataUnsafe.query_id: The unique query identifier for the session, used in inline mode.
# Telegram.WebApp.initDataUnsafe.auth_date: The Unix timestamp indicating when the data was generated.
# Telegram.WebApp.initDataUnsafe.hash: A hash string to validate the data integrity and authenticity.

# Inline Button Information (for bots launched from inline buttons)

# Telegram.WebApp.initDataUnsafe.inline_message_id: The ID of the inline message that opened the Web App (if applicable).
# Telegram.WebApp.initDataUnsafe.start_param: The start parameter that was passed to the bot when the Web App was opened.

# Web App Information

# Telegram.WebApp.isExpanded: Whether the Web App is expanded to the full height.
# Telegram.WebApp.viewportHeight: The height of the visible area of the Web App in pixels.
# Telegram.WebApp.viewportStableHeight: The stable height of the Web App when the virtual keyboard is not visible.