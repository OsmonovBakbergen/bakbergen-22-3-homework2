from aiogram import types, Dispatcher
from config import bot, dp

async def quiz_2(call: types.CallbackQuery):
    question = "Сколько будет 5+7?"
    answers = [
        "Одиннадцать",
        "Адиннадцать",
        "Я хз вообще"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Будет двеннадцать",
        open_period=10
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')