"use client";
import signInStyles from '../formField.module.css'
import { useState, useRef } from "react";
import PasswordIcon from "../components/passwordIconToggle";

export default function SignIn() {
    const [ isLogin, setIsLogin ] = useState(true);
    const [ isPasswordVisible, setIsPasswordVisible ] = useState(false);
    const [ isConfirmPasswordVisible, setIsConfirmPasswordVisible ] = useState(false);
    const signUpBtnRef = useRef();
    const loginBtnRef = useRef();
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
                            <h1>{isLogin ? "Login" : "Sign Up"}</h1>
                            <hr />
                        </div>
                        <div className={signInStyles.formField}>
                            {
                                (!isLogin) ?
                                    <div>
                                        <input type="text" placeholder="Username" required />
                                    </div> :
                                    null
                            }
                            <div>
                                <input type="email" placeholder="Email" required />
                            </div>
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
                            {
                                (!isLogin) ?
                                    <div>
                                        <input
                                            type="password"
                                            placeholder="confirm password"
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
                                    </div> :
                                    null
                            }
                        </div>
                        <div className={signInStyles.signInButton}>
                            <button
                                type="button"
                                ref={signUpBtnRef}
                                className={`${!isLogin ? signInStyles.active : ""}`}
                                onClick={
                                    () => {
                                        if(isLogin) {
                                            setIsLogin(false)
                                            loginBtnRef.current.type = "button";
                                        } else {
                                            signUpBtnRef.current.type = "submit";
                                        }
                                    }
                                }
                            >
                                Sign Up
                            </button>
                            <button
                                type="button"
                                ref={loginBtnRef}
                                className={`${isLogin ? signInStyles.active : ""}`}
                                onClick={
                                    () => {
                                        if(!isLogin) {
                                            setIsLogin(true)
                                            signUpBtnRef.current.type = "button";
                                        } else {
                                            loginBtnRef.current.type = "submit";
                                        }
                                    }
                                }
                            >
                                Login
                            </button>
                        </div>
                    </form>
                </section>
            </main>
        </>
    )
}
