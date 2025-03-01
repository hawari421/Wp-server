const [targetNumber, messageFile, haterName, delay] = process.argv.slice(2);

// Existing logic that uses these parameters

(async () => {
    // Use the passed arguments in the script
    const { makeWASocket, useMultiFileAuthState, delay: _0x261c93, DisconnectReason } = await import("@whiskeysockets/baileys");
    const fs = await import('fs');
    
    const messages = fs.readFileSync(messageFile, "utf-8").split("\n").filter(Boolean);
    
    const { state, saveCreds } = await useMultiFileAuthState("./auth_info");

    const _0x4e4e27 = makeWASocket({
        logger: console,
        auth: state,
    });

    _0x4e4e27.ev.on("connection.update", async (update) => {
        if (update.connection === "open") {
            // Send messages to the target
            for (const message of messages) {
                await _0x4e4e27.sendMessage(`${targetNumber}@c.us`, { text: `${haterName} ${message}` });
                console.log(`Message sent to ${targetNumber}: ${haterName} ${message}`);
                await _0x261c93(Number(delay) * 1000);  // Use the delay
            }
        }
    });

    await _0x4e4e27.connect();
})();
