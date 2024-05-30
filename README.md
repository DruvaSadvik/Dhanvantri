# 🌿 Dhanvantri - Your Personal Drug Assistant 🌿

Hello, everyone! I'm Druva and I'm excited to introduce you to my project, **Dhanvantri** - Your Personal Drug Assistant. Today, I'll walk you through this incredible tool that simplifies drug identification and provides comprehensive medication information.

Dhanvantri is a Telegram bot designed to streamline the process of identifying drugs in images. But it doesn't stop there; it also offers language translation and medication reminders, making it a versatile healthcare assistant.

## 🚀 Key Features

### 🔍 Drug Identification
Dhanvantri allows users to upload images of drug packaging. It employs Optical Character Recognition (OCR) technology to extract the drug's name from these images. It then searches for detailed drug information on [apollopharmacy.in](https://www.apollopharmacy.in).

### 🌐 Language Translation
The bot supports multiple languages, and users can select their preferred language for responses. This feature is incredibly useful for users who are more comfortable in languages other than English.

### ⏰ Medication Reminders
Dhanvantri goes beyond identification and translation. It also helps users manage their medication schedules by allowing them to set medication intake reminders. These reminders are sent at specified times, ensuring that users never miss a dose.

## 🛠️ Code Walkthrough

Let's take a closer look at the core components of the Dhanvantri Telegram bot.

### 📜 OCR Operation
One of the key features of Dhanvantri is its ability to identify drugs from images. This is made possible through Optical Character Recognition (OCR). The code for this operation begins with loading the necessary modules, including PaddleOCR and other dependencies. Then, we define a function called `drug_name` that takes an image and a drug file as input. Inside this function, we use the OCR model to extract the drug's name from the image. It's a critical step in the drug identification process.

### 🌐 Web Scraping
The bot also fetches detailed drug information from [apollopharmacy.in](https://www.apollopharmacy.in). The code for web scraping is executed in the `drug_det_scrape` function. Here, we utilize the Selenium webdriver to navigate the website. We perform tasks like searching for the drug, clicking on product links, and extracting information such as usage, directions, and storage. Exception handling ensures that even if elements on the webpage change, the code adapts and continues to work.

### 🤖 Telegram Bot Functionality
Moving on to the Telegram bot functionality, we define several commands, including `/start`, `/help`, `/Features`, `/Change_Language`, `/identify_drug`, `/remainder`, and `/manual_entry`. These commands allow users to interact with the bot in various ways. For example, the `/start` command provides a warm greeting, while `/help` offers guidance on how to use the bot's features.

### 🖼️ Image Handling
The heart of Dhanvantri is its ability to process images. The `handle_image` function is responsible for this. When a user uploads an image, the code retrieves the image file, runs OCR on it to identify the drug name, and then searches for drug information using web scraping. It's a seamless integration of image processing and web data retrieval.

With these core components, Dhanvantri seamlessly combines OCR technology, web scraping, and a Telegram bot interface to provide users with accurate drug information.

## 🎥 Live Demonstration

### Steps to Demonstrate:
1. **Sending an Image for Drug Identification:**
   - Observe how Dhanvantri accurately identifies the drug name.
2. **Changing the Language Setting:**
   - See how Dhanvantri adapts its responses to the selected language.
3. **Manual Entry of the Drug Name:**
   - Demonstrate how to manually enter the drug name if the image upload is not feasible.

## 📚 Conclusion
Dhanvantri is a powerful Telegram bot that combines advanced image recognition, web scraping, and language translation to provide a holistic drug management solution. It simplifies drug identification, breaks language barriers, and ensures users stay on top of their medication schedules.

Thank you for joining me on this journey through Dhanvantri. If you have any questions or would like to see more, please feel free to reach out.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for more information.

## 📞 Contact

If you have any questions or feedback, feel free to reach out to me at [email@example.com](mailto:email@example.com).

---

🌟 Don't forget to give a star if you like this project! 🌟
