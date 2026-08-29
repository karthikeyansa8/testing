const Textform = () => {
    const handlesubmit = async (e) => {
        e.preventDefault()
        console.log("Submitted")
        try {
            const response = await fetch("http://localhost:8000/form/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: e.target.name.value,
                    phone: e.target.phone.value,
                    email: e.target.email.value,
                    password: e.target.password.value
                })
            })
            const data = await response.json()
            console.log("Form submission response:", data)
        } catch (error) {
            console.error("Error submitting form:", error)
        }
    }

    return (
        <>
            <form onSubmit={handlesubmit}>
                <label htmlFor="name">Name :</label>
                <input name='name' id='name' type="text" />
                <label htmlFor="phone">Phone :</label>
                <input name='phone' id='phone' type="number" />
                <label htmlFor="email">Email :</label>
                <input name='email' id='email' type="email" />
                <label htmlFor="password">Password :</label>
                <input name='password' id='password' type="password" />
                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default Textform