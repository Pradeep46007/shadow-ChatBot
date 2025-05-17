import random
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

ecommerce_pairs = [
    [
        r"hi|hello|hey",
        ["👋 Hello! Welcome to our Shadow store. How can I assist you today?", 
         "Hi there! 😊 How can I help you with your shopping experience?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm functioning well! 🤖 How can I assist you today?",]
    ],
    [
        r"what products do you have|what do you sell|Product inquiries",
        ["🛒 We sell a variety of products including electronics, clothing, home goods, and more. Is there a specific category you're interested in?",]
    ],
    [
        r"order status|where is my order|track my order",
        ["📦 To check your order status, please provide your order number.", 
         "I can help with order tracking. 🚚 Please share your order ID."]
    ],
    [
        r"return policy|can I return|return|can I return this",
        ["🔄 Our return policy allows returns within 30 days of purchase with original receipt. Do you need help initiating a return?",]
    ],
    [
        r"payment options|how to pay|How can I pay",
        ["💳 We accept credit cards, PayPal, and bank transfers. Which payment method would you like to use?",]
    ],
    [
        r"shipping time|delivery time|when will I get|When will i get the product|when will i recieve the product|Shipping details",
        ["🚚 Standard shipping takes 3-5 business days. Express shipping is available for faster delivery.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! 😊 Is there anything else I can help you with?", 
         "Happy to help! 🙌 Let me know if you have other questions."]
    ],
    [
        r"discount|offer|promotion|sale",
        ["🎉 We have ongoing discounts and promotions! Please check our website's 'Offers' section for the latest deals."]
    ],
    [
        r"cancel order|how to cancel|can I cancel",
        ["To cancel your order, please provide your order number and I'll assist you further. ❌",]
    ],
    [
        r"change address|update address|wrong address",
        ["🏠 You can update your shipping address before the order is shipped. Please provide your order number for assistance.",]
    ],
    [
        r"contact support|customer care|phone number|email|What is your phone number",
        ["📞 You can reach our customer support at support@shadowstore.com or call us at 1-800-SHADOWS.",]
    ],
    [
        r"warranty|guarantee|product warranty|Warranty information|What is the warranty",
        ["🛡️ Most products come with a 1-year warranty. Would you like details for a specific product?",]
    ],
    [
        r"out of stock|when available|restock",
        ["🔔 If a product is out of stock, you can sign up for notifications on the product page. Would you like help with this?",]
    ],
    [
        r"track refund|refund status|where is my refund|refund",
        ["💸 Refunds are processed within 5-7 business days after approval. Please provide your order number for status updates.",]
    ],
    [
        r"exchange|replace|replacement policy|Exchange policy|How do I exchange an item",
        ["♻️ We offer exchanges for defective or incorrect items. Please provide your order number for assistance.",]
    ],
    [
        r"help|what can you do|support|i need help",
        ["🆘 I can assist you with: \n"
         "- Checking order status (e.g., 'Where is my order?') 📦\n"
         "- Product inquiries (e.g., 'What do you sell?') 🛒\n"
         "- Returns & refunds (e.g., 'Can I return this?') 🔄\n"
         "- Payment options (e.g., 'How can I pay?') 💳\n"
         "- Shipping details (e.g., 'When will i get the product') 🚚\n"
         "- Warranty information (e.g., 'What is the warranty?') 🛡️\n"
         "- Contact support (e.g., 'What is your phone number?') ☎️\n"
         "- Exchange policy (e.g., 'How do I exchange an item?') ♻️\n"
         "Type 'quit' to exit.",]
    ],
    [
        r"quit|bye|goodbye",
        ["Thank you for shopping with us! Have a great day! 🌟", 
         "Goodbye! 👋 Come back if you have more questions."]
    ],
]

def ecommerce_chatbot():
    print("Welcome to our Shadow customer support. Type 'help' for assistance or 'quit' to exit.")
    chat = Chat(ecommerce_pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    ecommerce_chatbot()