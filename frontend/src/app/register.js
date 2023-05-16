"use client";
import { useEffect } from "react";

export function RegisterPWA() {
    useEffect(() => {
        if ("serviceWorker" in navigator && window["workbox"] !== undefined) {
            const wb = window["workbox"];
            wb.register();
        }
    }, []);
    return (
        <></>
    )
}
