import streamlit as st

def main():
    st.title("📚 Test: ¿Qué tan nerd eres? 🤓")
    
    preguntas = [
        ("¿Cuál es el número atómico del oxígeno?", ["6", "7", "8", "9"], "8"),
        ("¿Quién formuló la teoría de la relatividad?", ["Isaac Newton", "Nikola Tesla", "Albert Einstein", "Stephen Hawking"], "Albert Einstein"),
        ("¿Qué planeta es conocido como el planeta rojo?", ["Venus", "Marte", "Júpiter", "Saturno"], "Marte"),
        ("¿Cuál es la raíz cuadrada de 144?", ["10", "12", "14", "16"], "12"),
        ("¿Quién escribió '1984' y 'Rebelión en la Granja'?", ["Aldous Huxley", "J.R.R. Tolkien", "George Orwell", "Ray Bradbury"], "George Orwell"),
        ("¿Cuál es el compuesto químico del agua?", ["CO2", "H2O", "O2", "NaCl"], "H2O"),
        ("¿Qué lenguaje de programación es conocido por su uso en ciencia de datos?", ["Java", "C++", "Python", "Ruby"], "Python"),
        ("¿Qué fuerza mantiene a los planetas en órbita alrededor del Sol?", ["Magnetismo", "Electromagnetismo", "Gravedad", "Inercia"], "Gravedad"),
        ("¿Quién pintó la Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
        ("¿Cuál es el hueso más largo del cuerpo humano?", ["Fémur", "Húmero", "Radio", "Tibia"], "Fémur")
    ]
    
    respuestas_correctas = 0
    
    for i, (pregunta, opciones, respuesta_correcta) in enumerate(preguntas):
        seleccion = st.radio(f"{i+1}. {pregunta}", opciones, key=f"pregunta_{i}")
        if seleccion == respuesta_correcta:
            respuestas_correctas += 1
    
    if st.button("Ver resultados"):
        porcentaje = (respuestas_correctas / len(preguntas)) * 100
        if porcentaje == 100:
            emoji = "🤯"
            st.info("Genio absoluto")
        elif porcentaje >= 80:
            emoji = "🤓"
            st.info("Súper nerd")
        elif porcentaje >= 50:
            emoji = "😃"
            st.info("Algo nerd")
        else:
            emoji = "🤡"
            st.info("Casi nada nerd")
        
        st.subheader(f"Obtuviste {respuestas_correctas} de {len(preguntas)} respuestas correctas.")
        st.subheader(f"Tu porcentaje de nerd es: {porcentaje:.2f}% {emoji}")
        
if __name__ == "__main__":
    main()
