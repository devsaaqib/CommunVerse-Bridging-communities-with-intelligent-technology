# CommunVerse-Bridging-communities-with-intelligent-technology
CommuneVerse is an AI-powered social media platform that goes beyond traditional networking — enabling intelligent, real-time conversations, personalized recommendations, and location-specific event discovery.
🚀 Overview
CommuneVerse is a next-generation AI-powered social platform designed not just to connect people, but to understand and assist them. It's a space where users don’t just post and scroll — they interact, discover, and engage through intelligent conversations and personalized recommendations.

Imagine a platform that chats with you, understands your interests, and shows you what's happening around you — that’s the power of CommuneVerse.

✨ Features
🧠 AI-Driven Conversations
Engage in real-time chat with an NLP-powered assistant that understands and responds like a true companion.

📍 Location-Based Discovery
Get geo-specific event recommendations and community updates tailored to your current location.

📈 Adaptive Learning
Machine learning enhances user experience over time by adapting based on feedback and behavior.

🎯 Personalized Recommendations
Suggestions are custom-tailored to individual interests and usage history.

⚡ Real-Time Interface
Enjoy smooth and instant interactions through a responsive chat system.

🔐 Secure & Efficient
Backend services are optimized for speed and safety with robust database management.


**CommuneVerse** is a comprehensive full-stack application designed to address the challenges of community discovery and engagement. It integrates advanced chatbot capabilities to help users discover events, activities, and community gatherings based on their interests and location.

What if your favorite social media app could also understand you, chat with you, and make your interactions smarter and more meaningful? That's exactly what we've built. Introducing a social media platform like no other — a place where artificial intelligence meets human connection, giving you the best of both worlds: **community and conversation**.

The application leverages cutting-edge technologies to provide:

1. **Natural Language Processing (NLP):** Enables the chatbot to understand and process user queries conversationally.
2. **Personalized Recommendations:** Tailored suggestions for events and activities based on user preferences and interaction history.
3. **Location-Based Discovery:** Utilizes geolocation services to provide personalized, geo-specific recommendations for community gatherings and events.
4. **Continuous Learning:** Incorporates machine learning to adapt and improve recommendations based on user feedback and behavior over time.



## Screen Shorts

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/f2d8f573-6621-4aa4-b060-fa03423fecd0" alt="Screenshot 1" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/b82c5519-6189-4584-b2cc-356c2b6fdecf" alt="Screenshot 2" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/a62120e6-a7b8-4acb-8680-4e55e9e6bf7a" alt="Screenshot 3" width="300"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/1267fc72-a67a-49d7-b48a-debfc50b8c40" alt="Screenshot 4" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/9ce0590a-81a2-4c2a-b0d2-4e85d022fda3" alt="Screenshot 5" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/1e0b1a48-0263-4fa5-a9f0-5d422a6d7649" alt="Screenshot 6" width="300"/></td>




  </tr>
</table>

## Prerequisites

### Tools and Dependencies
- **Node.js** (v14 or higher): Required for running the backend and frontend.
- **npm** (Node Package Manager): Comes with Node.js and is used for installing dependencies.
- **Git**: For version control (optional).

### Installations
1. [Download and install Node.js](https://nodejs.org/).
2. Clone this repository or extract the project files.

## Directory Structure
```
kynnovative_project/
│
├── communeVerse-frontend/  # Frontend application
│   ├── public/            # Static assets
│   ├── src/               # Source code
│   ├── .env.local         # Frontend-specific environment variables
│   └── package.json       # Frontend dependencies
│
├── communeVerse-backend/   # Backend application
│   ├── app.js             # Main backend server file
│   ├── .env               # Backend-specific environment variables
│   └── package.json       # Backend dependencies
│
└── README.md               # Project documentation
```

## Setup Instructions

### 1. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd kynnovative_project/communeVerse-backend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Configure the environment variables:
   - Create a `.env` file in the backend directory with the required keys. Refer to `.env.example` if available.
   - Ensure the `.env` file includes:
     - `PORT`: Port number for the backend server (default: 5000).
     - `OPENAI_API_KEY`: API key for OpenAI integrations.
     - `DATABASE_URL`: Connection URL for the MySQL database.

4. Start the backend server:
   ```bash
   node app.js
   ```
   The backend server should now be running on the specified port (e.g., `http://localhost:5000`).

### 2. Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../communeVerse-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Configure the environment variables:
   - Create a `.env.local` file in the frontend directory with the required keys. Refer to `.env.local.example` if available.
   - Ensure the `.env.local` file includes:
     - `NEXT_PUBLIC_API_URL`: Backend API base URL (e.g., `http://localhost:5000`).

4. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend server should now be running on `http://localhost:3000`.

## Running the Project
1. Start the backend server as described above.
2. Start the frontend server.
3. Open a browser and navigate to `http://localhost:3000` to access the application.

## Environment Variables

### Backend
Ensure the `.env` file includes:
- `PORT`: Port number for the backend server (default: 5000).
- `OPENAI_API_KEY`: API key for OpenAI integrations.
- `DATABASE_URL`: URL for the MySQL database.

### Frontend
Ensure the `.env.local` file includes:
- `NEXT_PUBLIC_API_URL`: Backend API base URL (e.g., `http://localhost:5000`).

## Troubleshooting
- **Issue**: `npm install` fails.
  - **Solution**: Ensure you are using a supported Node.js version. Try deleting `node_modules` and `package-lock.json`, then reinstall dependencies.

- **Issue**: Environment variables not recognized.
  - **Solution**: Verify the `.env` and `.env.local` files are correctly formatted and saved.

## Technologies Used

### Frontend:
- **Next.js**: React-based framework for building fast and dynamic user interfaces.
- **React.js**: Component-based library for creating interactive and reusable UI components.
- **CSS Modules**: Scoped and maintainable styling for application components.

### Backend:
- **Node.js**: Server-side runtime for scalable and efficient backend development.
- **Express.js**: Minimal and flexible Node.js framework for building APIs.
- **OpenAI API**: Provides advanced conversational AI capabilities to enhance chatbot functionality.

### Database:
- **MySQL**: Relational database management system for efficient and structured data storage and retrieval.

### Environment Management:
- **dotenv**: Securely manages environment variables for API keys and configurations.

### API Integration:
- **OpenAI**: For intelligent natural language processing and chatbot interactions.
- **Geolocation APIs**: To enable location-based discovery of events and activities.

### Version Control:
- **Git**: For version control and collaborative development.
- **GitHub**: Repository hosting for managing the project codebase.

### Development Tools:
- **npm**: Node Package Manager for dependency management.
- **VS Code**: Primary code editor for development.


🧰 Tech Stack
🔹 Frontend
Next.js – React-based framework for dynamic, SEO-friendly pages.

CSS Modules – Modular and scoped styling.

Responsive Design – Accessible across mobile, tablet, and desktop devices.

🔹 Backend
Node.js

Express.js – Handles API requests and routing.

OpenAI API – For intelligent conversational capabilities.

dotenv – Manages secure environment variables.

🔹 Database
MySQL – Structured, relational data storage for user data, interactions, and preferences.

🛠️ How It Works
User logs in and shares interests.

The AI assistant chats with the user, providing personalized event recommendations.

Geolocation is used to tailor content and activities based on the user’s location.

Feedback is collected to refine future recommendations via adaptive ML algorithms.

🌍 Use Cases
Event Management: Discover events around your city based on your interests.

Community Building: Connect with like-minded people in real time.

Social Networking: Engage in meaningful conversations, powered by AI.

👤 User Benefits
Tailored Experience – Personalized chat and suggestions.

Geo-Aware Interaction – Relevant updates wherever you are.

Instant Communication – Real-time chat interface.

Smarter Over Time – Adaptive learning from user interactions.

Scalable and Versatile – Can be adapted for various domains like corporate networking or public engagement.

Multilingual Ready – Future support for diverse user bases.

🔗 Integration with Other Platforms
CommuneVerse can be seamlessly integrated with existing platforms like KYN to:

Enhance user engagement via personalized AI chats.

Expand reach through smart recommendations.

Support multilingual communities.

⚠️ Challenges Faced
OpenAI API integration – Ensuring natural and responsive conversation.

Geolocation accuracy – Delivering location-relevant suggestions.

Data optimization – Efficiently managing user preferences and feedback.

Secure frontend-backend communication.

🔮 Future Scope
🌐 Multilingual Support

🧑‍💼 Corporate Networking Customization

🤖 Advanced AI for deeper personalization

📸 Screenshots & Demo
Coming Soon

🤝 Contributing
We welcome contributions! To get started:

Fork the repo

Clone the repo

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature-name)

Open a pull request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For feedback or inquiries:
📧 Email: dev.saaqib17@gmail.com
🔗 LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/saaqib-a-19228b205/)
