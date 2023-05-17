"use client";
import signInStyles from '../formField.module.css'
import { useState, useRef } from "react";
import PasswordIcon from "../components/passwordIconToggle";

export default function ForgotPassword() {
    const [ isPasswordVisible, setIsPasswordVisible ] = useState(false);
    const [ isConfirmPasswordVisible, setIsConfirmPasswordVisible ] = useState(false);
    const passwordRef = useRef();
    const confirmPasswordRef = useRef();

    return (
        <>
            <main className={signInStyles.main}>
                <section className={signInStyles.signInContainer}>
                    <form
                        className={signInStyles.form}
                        onSubmit={(e)=> {
                            e.preventDefault();
                            console.log("SUBMIT");
                        }}
                    >
                        <div className={signInStyles.formTitle}>
                            <h1>Forgot Password</h1>
                            <hr />
                        </div>
                        <div className={signInStyles.formField}>
                            <div>
                                <input type="password" placeholder="Password" required ref={passwordRef} />
                                <button
                                    className={signInStyles.viewPassword}
                                    type="button"
                                    title="toggle password visibility"
                                    onClick={
                                        ()=> {

                                            if(passwordRef.current.type === "text") {
                                                setIsPasswordVisible(false);
                                                passwordRef.current.type = "password";
                                            } else {
                                                setIsPasswordVisible(true);
                                                passwordRef.current.type = "text";
                                            }
                                        }
                                    }
                                >
                                    <PasswordIcon show={isPasswordVisible} />
                                </button>
                            </div>
                            <div>
                                <input
                                    type="password"
                                    placeholder="confirm password"
                                    required
                                    ref={confirmPasswordRef}
                                />
                                <button
                                    className={signInStyles.viewPassword}
                                    type="button"
                                    title="toggle password visibility"
                                    onClick={
                                        ()=> {

                                            if(confirmPasswordRef.current.type === "text") {
                                                setIsConfirmPasswordVisible(false);
                                                confirmPasswordRef.current.type = "password";
                                            } else {
                                                setIsConfirmPasswordVisible(true);
                                                confirmPasswordRef.current.type = "text";
                                            }
                                        }
                                    }
                                >
                                    <PasswordIcon show={isConfirmPasswordVisible} />
                                </button>
                            </div>
                        </div>
                        <div
                            className={`
                                ${signInStyles.signInButton}
                                ${signInStyles.forgotPasswordButton}
                            `}
                        >
                            <button
                                type="submit"
                                onClick={
                                    () => {}
                                }
                            >
                                Submit
                            </button>
                        </div>
                    </form>
                </section>
            </main>
        </>
    )
}
