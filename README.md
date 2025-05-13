# AI-Based Crowd Sentiment Analysis for Protests & Gatherings

> *Empowering Civic Safety Through Emotion-Aware Intelligence*

---

## 🚨 Problem Statement

Governments and organizations often struggle to understand crowd sentiment in real-time during protests, public events, or large gatherings. This lack of insight can delay response times and escalate conflicts.

---

## 💡 Proposed Solution

This system uses **AI-powered video analysis** to detect emotional states in crowds, helping authorities and event organizers make informed, timely decisions.

In addition to video analysis, the system also implements **text-based sentiment analysis** using a dataset of protest-related tweets (`protest_tweets.csv`). This helps provide a **broader, multi-modal understanding of crowd sentiment** by combining visual emotion recognition with **NLP-based tweet sentiment mining**.


### 📌 Phase Implementation:
- **Phase 1**: Social media or stored video sentiment analysis using NLP and facial emotion recognition.
- **Phase 2**: Live video feed analysis, with real-time heatmaps and agitation detection.

---

## ✅ Key Features

- Real-time emotion detection from crowd footage  
- Heatmap generation showing zones of agitation or peace  
- Integration with social media videos for crowd sentiment mining  
- Predictive riot risk analysis using emotion trends

---

## 🛠 Tech Stack

| Layer               | Technology                 |
|--------------------|----------------------------|
| Video Analysis      | OpenCV, DeepFace           |
| Emotion Detection   | AffectNet, TensorFlow      |
| NLP Sentiment       | TextBlob, Scikit-learn     |
| Visualization       | Matplotlib, Seaborn        |
| Backend Scripting   | Python                     |

---

---

## 🔁 Work Flow 

1. Input video (live or uploaded)
2. Face detection and emotion recognition using DeepFace
3. Sentiment aggregation
4. Heatmap and emotional intensity chart generation
5. Report and visualization output

---

## 🎯 Usefulness & Scalability

### Usefulness:
- Real-time crowd mood monitoring
- Preventive control in large gatherings
- Helpful for public safety teams and event organizers

### Scalability:
- Compatible with multiple live feeds
- Can work with different cities/regions
- Easily integrates with surveillance & social media

---

## 📥 Input Example

ProtestVideo2.mp4
we can add any other protest videos

---

## 📤 Output Example

- Emotion Log CSV: `outputs/emotion_log.csv`
- Heatmap and visualizations (auto-generated)
![Screenshot (11)](https://github.com/user-attachments/assets/3c8f5d52-a224-455c-8c8e-b9eb7ccb10b0)
![Screenshot (12)](https://github.com/user-attachments/assets/0701af00-3988-4114-a19c-73ce24282765)
![Screenshot (10)](https://github.com/user-attachments/assets/18436cf4-6684-4e0f-90e5-4a6c6fa6f004)

---

## ⚙️ Technical Challenges & Solutions

| Challenge                | Solution                            |
|--------------------------|-------------------------------------|
| Low-light video input    | Enhanced model tuning, histogram EQ |
| Model bias               | Diverse datasets like AffectNet     |
| Large file processing    | Frame sampling, async reading       |
| Real-time performance    | GPU acceleration, optimized loops   |

---

## 🚀 Future Enhancements

- Live dashboard for public authorities
- Integration with drone or CCTV footage
- Real-time riot alert system
- NLP on protester chants and tweets

---

## 📊 Feasibility Study

| Area         | Feasibility                           |
|--------------|----------------------------------------|
| Technical    | Achievable with OpenCV + DeepFace     |
| Operational  | Deployable with minimal resources      |
| Economic     | Open-source tools keep costs low       |

---

## 🧠 Built With ❤️ by Team 

- Sona S
- Vaishnavi S
- Subhalakshmi C
- Regi Rufina JD

**Saranathan College of Engineering**

---

## 📬 Contact Us

- subha03062005@gmail.com  
- sonaskh001@gmail.com  
- regirufinajd@gmail.com  
- vaishnavi@gmail.com 

---

# Let's Make Protests Safer with AI-Powered Awareness 🔍
