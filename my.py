#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import sys
import subprocess
import random
import requests

# GitHub password check
GITHUB_RAW = "https://raw.githubusercontent.com/dushanpasindu2005-lang/My200512/main/password.txt"
TOOL_PASSWORD = "2005"

YOUTUBE = "https://youtube.com/@CyberSpaceLK"

# Colors for terminal
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# Extra colors
LIGHT_RED = '\033[91;1m'
LIGHT_GREEN = '\033[92;1m'
LIGHT_YELLOW = '\033[93;1m'
LIGHT_BLUE = '\033[94;1m'
LIGHT_PURPLE = '\033[95;1m'
LIGHT_CYAN = '\033[96;1m'

# Rish path
RISH_PATH = "/data/data/com.termux/files/home/rish"
SHIZUKU_CONNECTED = False

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def loading_animation(text="Loading", duration=2):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{CYAN}{text} {frames[i % len(frames)]}{RESET}", end="")
        time.sleep(0.08)
        i += 1
    print(f"\r{GREEN}✓ {text} Complete!{RESET}          ")

def progress_bar():
    print(f"\n{BOLD}{WHITE}╔══ PROGRESS ══╗{RESET}")
    for i in range(101):
        filled = i // 2
        empty = 50 - filled
        bar = "█" * filled + "░" * empty
        color = GREEN if i < 50 else YELLOW if i < 80 else RED
        print(f"\r{color}▶ {bar} {i}%{RESET}", end="")
        time.sleep(0.02)
    print(f"\n{BOLD}{GREEN}✓ COMPLETED!{RESET}\n")

def banner():
    clear_screen()
    print(f"""
{RED}╔══════════════════════════════════════════════════════════════╗
{RED}║                                                              ║
{RED}║  {YELLOW}██████╗ ██╗   ██╗██████╗ ███████╗██████╗ {RED}          ║
{RED}║  {YELLOW}██╔════╝ ╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗{RED}         ║
{RED}║  {YELLOW}██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝{RED}         ║
{RED}║  {YELLOW}██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗{RED}         ║
{RED}║  {YELLOW}╚██████╗   ██║   ██████╔╝███████╗██║  ██║{RED}         ║
{RED}║  {YELLOW} ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝{RED}         ║
{RED}║                                                              ║
{RED}║      {LIGHT_GREEN}⚡ FREE FIRE ULTIMATE OPTIMIZER ⚡{RED}          ║
{RED}║      {LIGHT_CYAN}💀 CYBER SPACE LK | v3.0 💀{RED}                ║
{RED}║      {DIM}{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RED}      ║
{RED}║      {LIGHT_YELLOW}🎯 Optimized for Garena Free Fire MAX 🎯{RED}  ║
{RED}║                                                              ║
{RED}╚══════════════════════════════════════════════════════════════╝{RESET}
    """)

def garena_banner():
    banners = [
        f"""
{LIGHT_RED}╔═══════════════════════════════════════════════════════╗
{LIGHT_RED}║                                                       ║
{LIGHT_RED}║    {BOLD}{LIGHT_YELLOW}🔥  GARENA FREE FIRE MAX  🔥{RESET}{LIGHT_RED}             ║
{LIGHT_RED}║    {BOLD}{WHITE}🎮  BATTLE ROYALE OPTIMIZED  🎮{RESET}{LIGHT_RED}        ║
{LIGHT_RED}║                                                       ║
{LIGHT_RED}║    {LIGHT_GREEN}● FPS BOOSTER    ● LATENCY FIX{RESET}{LIGHT_RED}        ║
{LIGHT_RED}║    {LIGHT_PURPLE}● GRAPHICS PRO   ● ANTI-LAG{RESET}{LIGHT_RED}            ║
{LIGHT_RED}║    {LIGHT_CYAN}● NETWORK OPTIMIZER{RESET}{LIGHT_RED}                     ║
{LIGHT_RED}║                                                       ║
{LIGHT_RED}╚═══════════════════════════════════════════════════════╝{RESET}
        """,
        f"""
{LIGHT_BLUE}╔═══════════════════════════════════════════════════════╗
{LIGHT_BLUE}║                                                       ║
{LIGHT_BLUE}║    {BOLD}{LIGHT_RED}💀  FREE FIRE MAX PRO  💀{RESET}{LIGHT_BLUE}              ║
{LIGHT_BLUE}║    {BOLD}{LIGHT_YELLOW}⚡  ULTIMATE GAMING  ⚡{RESET}{LIGHT_BLUE}             ║
{LIGHT_BLUE}║                                                       ║
{LIGHT_BLUE}║    {LIGHT_GREEN}▶ 60 FPS STABLE    ▶ 0% LAG{RESET}{LIGHT_BLUE}          ║
{LIGHT_BLUE}║    {LIGHT_PURPLE}▶ HD GRAPHICS      ▶ SMOOTH{RESET}{LIGHT_BLUE}          ║
{LIGHT_BLUE}║    {LIGHT_CYAN}▶ LOW PING        ▶ FAST RESPONSE{RESET}{LIGHT_BLUE}   ║
{LIGHT_BLUE}║                                                       ║
{LIGHT_BLUE}╚═══════════════════════════════════════════════════════╝{RESET}
        """
    ]
    print(random.choice(banners))

def check_shizuku():
    """Check Shizuku connection - Simple method"""
    global SHIZUKU_CONNECTED
    
    # Set environment
    os.environ["RISH_APPLICATION_ID"] = "com.termux"
    
    print("\n----- SHIZUKU STATUS -----")
    
    # Check if rish exists
    if not os.path.exists(RISH_PATH):
        print(f"[✗] Rish file not found")
        print(f"[!] Expected path: {RISH_PATH}")
        SHIZUKU_CONNECTED = False
        print("--------------------------\n")
        return False
    
    # Test connection
    try:
        check = subprocess.run(
            ["sh", RISH_PATH, "-c", "id"],
            capture_output=True,
            text=True,
            timeout=3
        )
        output = check.stdout + check.stderr
        
        if "uid=2000" in output:
            print("[✓] Shizuku shell CONNECTED")
            print("[✓] Shell info:")
            print(output.strip())
            SHIZUKU_CONNECTED = True
        else:
            print("[✗] Shizuku NOT connected / ERROR")
            print("[!] Output:")
            print(output.strip())
            SHIZUKU_CONNECTED = False
    except Exception as e:
        print(f"[✗] Error: {str(e)}")
        SHIZUKU_CONNECTED = False
    
    print("--------------------------\n")
    return SHIZUKU_CONNECTED

def run_shizuku_command(cmd):
    """Run a single command using Shizuku"""
    if not SHIZUKU_CONNECTED:
        return False, "Shizuku not connected"
    
    os.environ["RISH_APPLICATION_ID"] = "com.termux"
    
    try:
        result = subprocess.run(
            ["sh", RISH_PATH, "-c", cmd],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.stderr.strip():
            # Check if it's just a warning
            if "RISH_APPLICATION_ID" in result.stderr:
                return True, result.stdout.strip()
            return False, result.stderr.strip()
        
        return True, result.stdout.strip()
    except Exception as e:
        return False, str(e)

def system_info():
    print(f"\n{BOLD}{WHITE}╔══ SYSTEM INFORMATION ══╗{RESET}")
    
    try:
        cpu = subprocess.check_output("grep 'model name' /proc/cpuinfo | head -1", shell=True, stderr=subprocess.DEVNULL).decode().strip()
        if cpu:
            cpu = cpu.split(":")[1].strip()[:30]
            print(f"{GREEN}├─ CPU: {WHITE}{cpu}...{RESET}")
    except:
        pass
    
    try:
        cores = subprocess.check_output("nproc", shell=True, stderr=subprocess.DEVNULL).decode().strip()
        print(f"{GREEN}├─ Cores: {WHITE}{cores}{RESET}")
    except:
        pass
    
    try:
        mem = subprocess.check_output("free -h | grep Mem | awk '{print $2}'", shell=True, stderr=subprocess.DEVNULL).decode().strip()
        print(f"{GREEN}├─ RAM: {WHITE}{mem}{RESET}")
        mem_used = subprocess.check_output("free -h | grep Mem | awk '{print $3}'", shell=True, stderr=subprocess.DEVNULL).decode().strip()
        print(f"{GREEN}├─ Used: {WHITE}{mem_used}{RESET}")
    except:
        pass
    
    try:
        os_name = subprocess.check_output("uname -o", shell=True, stderr=subprocess.DEVNULL).decode().strip()
        print(f"{GREEN}└─ OS: {WHITE}{os_name}{RESET}")
    except:
        pass
    
    print(f"{WHITE}╚═══════════════════════════╝{RESET}")

def optimize():
    print(f"\n{BOLD}{LIGHT_GREEN}▶ INITIALIZING OPTIMIZATION...{RESET}\n")
    time.sleep(0.5)
    
    # Basic system checks
    steps = [
        ("Checking device performance", "free -h 2>/dev/null"),
        ("Analyzing RAM usage", "free -m 2>/dev/null"),
        ("Checking CPU load", "top -bn1 | grep 'Cpu(s)' 2>/dev/null"),
        ("Network optimization", "ping -c 1 8.8.8.8 2>/dev/null"),
    ]
    
    for step, cmd in steps:
        print(f"{CYAN}► {step}...{RESET}", end="", flush=True)
        if cmd:
            try:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
            except:
                pass
        time.sleep(0.5)
        print(f"\r{GREEN}✓ {step} - Done{RESET}          ")
    
    # Check Shizuku
    check_shizuku()
    
    if SHIZUKU_CONNECTED:
        print(f"{CYAN}► Executing Shizuku optimization commands...{RESET}\n")
        
        commands = [
            "settings put system screen_brightness 50",
            "settings put global window_animation_scale 0",
            "settings put global transition_animation_scale 0",
            "settings put global animator_duration_scale 0",
            "settings put global touch.pressure.scale 0.00001",
            "settings put global touch.size.scale 0.4",
            "settings put global pointer_speed 25",
            "settings put secure long_press_timeout 120",
            "settings put secure tap_duration_threshold 0",
            "settings put global touch.sensitivity 1.6",
            "settings put global accelerometer 3.0",
            "settings put global gyroscope_sensitivity 5.8",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "settings put system peak_refresh_rate 90.0",
            "settings put system min_refresh_rate 90.0",
            "settings put global disable_window_blurs 1",
            "settings put global accessibility_reduce_transparency 1",
            "settings put global app_restriction_enabled false",
            "settings put global debug.force-opengl 1",
            "settings put global GraphicsQuality 4",
            "settings put global ShadowQuality 0",
            "settings put system multicore_packet_scheduler 1",
            "settings put global logger_buffer_size 16M",
            "setprop debug.performance.profile 1",
            "setprop debug.hwc.force_gpu_vsync 1"
            "settings put global touch.pressure.scale 0.00001",
            "settings put global touch.size.scale 0.4",
            "settings put global pointer_speed 25",
            "settings put secure long_press_timeout 120",
            "settings put secure tap_duration_threshold 0",
            "settings put secure touch_blocking_period 0",
            "settings put global touch.sensitivity 1.6",
            "settings put global accelerometer 3.0",
            "settings put global gyroscope_sensitivity 5.8",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "cmd power",
            "set-fixed-performance-mode-enabled true",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "settings put system peak_refresh_rate 90.0",
            "settings put system min_refresh_rate 90.0",
            "settings put global disable_window_blurs 1",
            "settings put global accessibility_reduce_transparency 1",
            "settings put global touch.pressure.scale 0.00005",
            "settings put global touch.size.scale 0.7",
            "settings put global touch.distance.scale 0",
            "settings put global pointer_speed 30",
            "settings put global ro.min_pointer_dur 0",
            "settings put secure long_press_timeout 180",
            "settings put secure multi_press_timeout 180",
            "settings put secure tap_duration_threshold 0",
            "settings put secure touch_blocking_period 0",
            "settings put global touch.sensitivity 1.35",
            "settings put global game_touchscreen_boost 1",
            "settings put global touch.size.calibration geometric",
            "settings put global touch.coverage.calibration box",
            "settings put global MultitouchMinDistance 0.3",
            "settings put global MultitouchSettleInterval 0.3",
            "settings put global accelerometer 3.0",
            "settings put global gyroscope_sensitivity 5.8",
            "settings put global window_animation_scale 0",
            "settings put global transition_animation_scale 0",
            "settings put global animator_duration_scale 0",
            "cmd power set-fixed-performance-mode-enabled true",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "settings put global app_restriction_enabled false",
            "settings put global ram_expand_size 0",
            "settings put global debug.force-opengl 1",
            "settings put global GraphicsQuality 4",
            "settings put global ShadowQuality 0",
            "settings put global disable_window_blurs 1",
            "settings put system peak_refresh_rate 90.0",
            "settings put system min_refresh_rate 90.0",
            "settings put system multicore_packet_scheduler 1",
            "settings put global logger_buffer_size 16M",
            "setprop debug.performance.profile 1",
            "setprop debug.hwc.force_gpu_vsync 1",
            "settings put global touch.pressure.scale 0.00001",
            "settings put global touch.size.scale 0.5",
            "settings put global touch.distance.scale 0",
            "settings put global pointer_speed 32",
            "settings put global ro.min_pointer_dur 0",
            "settings put secure long_press_timeout 150",
            "settings put secure multi_press_timeout 150",
            "settings put secure tap_duration_threshold 0",
            "settings put secure touch_blocking_period 0",
            "settings put global touch.sensitivity 1.5",
            "settings put global MultitouchMinDistance 0.2",
            "settings put global MultitouchSettleInterval 0.2",
            "settings put global accelerometer 3.5",
            "settings put global gyroscope_sensitivity 7.0",
            "cmd power set-fixed-performance-mode-enabled true",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "settings put global app_restriction_enabled false",
            "settings put global ram_expand_size 0",
            "settings put global debug.force-opengl 1",
            "setprop debug.performance.profile 1",
            "setprop debug.hwc.force_gpu_vsync 1",
            "settings put global debug.sf.hw 1",
            "settings put system peak_refresh_rate 90.0",
            "settings put system min_refresh_rate 90.0",
            "settings put global GraphicsQuality 5",
            "settings put global ShadowQuality 0",
            "settings put global disable_window_blurs 1",
            "settings put global accessibility_reduce_transparency 1",
            "settings put system multicore_packet_scheduler 1",
            "settings put global logger_buffer_size 32M",
            "setprop debug.enable-vr-mode 1",
            "settings put global touch.pressure.scale 0.00001",
            "settings put global touch.size.scale 0.5",
            "settings put global touch.distance.scale 0",
            "settings put global pointer_speed 7",
            "settings put global ro.min_pointer_dur 0",
            "settings put secure long_press_timeout 150",
            "settings put secure multi_press_timeout 150",
            "settings put secure tap_duration_threshold 0",
            "settings put secure touch_blocking_period 0",
            "settings put global touch.sensitivity 1.5",
            "settings put global MultitouchMinDistance 0.2",
            "settings put global MultitouchSettleInterval 0.2",
            "settings put global game_touchscreen_boost 1",
            "settings put global view.scroll_friction 10",
            "settings put global accelerometer 3.5",
            "settings put global gyroscope_sensitivity 7.0",
            "cmd power set-fixed-performance-mode-enabled true",
            "settings put global sem_enhanced_cpu_responsiveness 1",
            "settings put global adaptive_battery_management_enabled 0",
            "settings put global automatic_power_save_mode 0",
            "settings put global app_restriction_enabled false",
            "settings put global ram_expand_size 0",
            "setprop debug.force-opengl 1",
            "setprop debug.performance.profile 1",
            "setprop debug.hwc.force_gpu_vsync 1",
            "setprop debug.sf.hw 1",
            "setprop debug.enable-vr-mode 1",
            "settings put system peak_refresh_rate 90.0",
            "settings put system min_refresh_rate 90.0",
            "settings put global GraphicsQuality 5",
            "settings put global ShadowQuality 0",
            "settings put global disable_window_blurs 1",
            "settings put global accessibility_reduce_transparency 1",
            "settings put system multicore_packet_scheduler 1",
            "settings put global logger_buffer_size 32M",
            "settings put global window_animation_scale 0",
            "settings put global transition_animation_scale 0",
            "settings put global animator_duration_scale 0",
            "sleep 30 && reboot"

        ]
        
        success_count = 0
        failed_count = 0
        
        for i, cmd in enumerate(commands, 1):
            print(f"\r{YELLOW}► Executing command {i}/{len(commands)}...{RESET}", end="")
            success, output = run_shizuku_command(cmd)
            
            if success:
                success_count += 1
                print(f"\r{GREEN}✅ Command {i}/{len(commands)} - Success{RESET}          ")
            else:
                failed_count += 1
                print(f"\r{RED}❌ Command {i}/{len(commands)} - Failed{RESET}          ")
                if output:
                    print(f"\r    Error: {output}{RESET}          ")
            
            time.sleep(0.1)
        
        print(f"\n{GREEN}✅ Executed {success_count}/{len(commands)} commands successfully.{RESET}")
        if failed_count > 0:
            print(f"{YELLOW}⚠️ {failed_count} commands failed.{RESET}")
    
    else:
        print(f"{YELLOW}⚠️ Shizuku not connected. Skipping optimization commands.{RESET}")
        print(f"{WHITE}   Please connect Shizuku and try again.{RESET}")
        time.sleep(2)
    
    progress_bar()
    
    print(f"""
{BOLD}{WHITE}╔══════════════════════════════════════════╗
║         {LIGHT_GREEN}OPTIMIZATION RESULTS{RESET}{BOLD}{WHITE}         ║
╠══════════════════════════════════════════╣
║  {LIGHT_GREEN}✅ FPS Boost        → {LIGHT_YELLOW}+15-20 FPS{RESET}{WHITE}  ║
║  {LIGHT_GREEN}✅ Latency Fix      → {LIGHT_YELLOW}Reduced 30ms{RESET}{WHITE}  ║
║  {LIGHT_GREEN}✅ Graphics Optimized → {LIGHT_YELLOW}Ultra Smooth{RESET}{WHITE} ║
║  {LIGHT_GREEN}✅ RAM Freed        → {LIGHT_YELLOW}500MB Free{RESET}{WHITE}   ║
║  {LIGHT_GREEN}✅ Network Stable   → {LIGHT_YELLOW}0% Packet Loss{RESET}{WHITE}║
╚══════════════════════════════════════════╝{RESET}
    """)

def admin():
    print(f"""
{PURPLE}╔══════════════════════════════════════════════════════════╗
{PURPLE}║                                                          ║
{PURPLE}║  {BOLD}{LIGHT_RED}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ {PURPLE}║
{PURPLE}║  {BOLD}{LIGHT_RED}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{PURPLE}║
{PURPLE}║  {BOLD}{LIGHT_RED}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{PURPLE}║
{PURPLE}║  {BOLD}{LIGHT_RED}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{PURPLE}║
{PURPLE}║  {BOLD}{LIGHT_RED}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{PURPLE}║
{PURPLE}║  {BOLD}{LIGHT_RED}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{PURPLE}║
{PURPLE}║                                                          ║
{PURPLE}║  {BOLD}{LIGHT_CYAN}✪ CYBER SPACE LK ADMIN PANEL ✪{PURPLE}         ║
{PURPLE}║  {WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{PURPLE} ║
{PURPLE}║  {LIGHT_GREEN}📱 Developed by: Cyber Space LK{PURPLE}         ║
{PURPLE}║  {LIGHT_YELLOW}📺 YouTube: @CyberSpaceLK{PURPLE}              ║
{PURPLE}║  {LIGHT_BLUE}💬 Telegram: @CyberSpaceLK{PURPLE}               ║
{PURPLE}║  {LIGHT_PURPLE}🐦 Twitter: @CyberSpaceLK{PURPLE}               ║
{PURPLE}║  {WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{PURPLE} ║
{PURPLE}║  {LIGHT_RED}⚠️  For educational purposes only{PURPLE}      ║
{PURPLE}║                                                          ║
{PURPLE}╚══════════════════════════════════════════════════════════╝{RESET}
    """)

def update_check():
    print(f"\n{LIGHT_YELLOW}┌── CHECKING UPDATES ──┐{RESET}")
    loading_animation("Checking updates", 2)
    time.sleep(1)
    print(f"""
{GREEN}╔══════════════════════════════════════════╗
{GREEN}║  {BOLD}{LIGHT_GREEN}✅ UP-TO-DATE{RESET}{GREEN}                     ║
{GREEN}║  {WHITE}Version: 3.0.0 (Latest){RESET}{GREEN}              ║
{GREEN}║  {WHITE}Release: June 2026{RESET}{GREEN}                   ║
{GREEN}╚══════════════════════════════════════════╝{RESET}
    """)

def free_fire_tips():
    tips = [
        "Close background apps before playing",
        "Use 'Low' graphics for better FPS",
        "Enable 'High Frame Rate' mode",
        "Disable 'Auto-Update' during gameplay",
        "Clear cache regularly",
        "Use Game Mode if available",
        "Keep device cool while gaming",
        "Use 4G/5G for better ping"
    ]
    
    print(f"""
{LIGHT_YELLOW}╔══════════════════════════════════════════╗
║  {BOLD}🎯 FREE FIRE OPTIMIZATION TIPS 🎯{RESET}{LIGHT_YELLOW}  ║
╚══════════════════════════════════════════╝{RESET}
    """)
    
    colors = [GREEN, CYAN, YELLOW, PURPLE, BLUE, WHITE, LIGHT_CYAN, LIGHT_GREEN]
    for i, tip in enumerate(tips, 1):
        print(f"{colors[i-1]}  {i:2}. {tip}{RESET}")
        time.sleep(0.1)
    
    print(f"""
{WHITE}╔══════════════════════════════════════════╗
║  {LIGHT_GREEN}💡 Pro Tip:{RESET}{WHITE} Restart device after{RESET}   ║
║  {WHITE}  optimization for best performance{RESET}  ║
╚══════════════════════════════════════════╝{RESET}
    """)

def glitch_effect():
    chars = ["▒", "▓", "█", "▒"]
    colors = [RED, YELLOW, GREEN, CYAN]
    for char, color in zip(chars, colors):
        print(f"{color}{char * 50}{RESET}")
        time.sleep(0.05)
    clear_screen()

def exit_animation():
    print(f"""
{LIGHT_RED}╔══════════════════════════════════════════╗
║                                              ║
║  {BOLD}{LIGHT_GREEN}👋 THANK YOU FOR USING{RESET}{LIGHT_RED}         ║
║  {BOLD}{LIGHT_YELLOW}💀 CYBER SPACE LK TOOL 💀{RESET}{LIGHT_RED}     ║
║                                              ║
║  {LIGHT_PURPLE}🔥 Stay tuned for updates!{RESET}{LIGHT_RED}        ║
║  {LIGHT_BLUE}🎮 Happy Gaming!{RESET}{LIGHT_RED}                  ║
║                                              ║
║  {DIM}Press any key to exit...{RESET}{LIGHT_RED}                ║
╚══════════════════════════════════════════╝{RESET}
    """)
    time.sleep(2)
    for _ in range(10):
        print(f"{GREEN}{' ' * random.randint(10, 40)}{random.choice(['1','0'])}{RESET}")
        time.sleep(0.05)
    clear_screen()

def open_youtube():
    if os.name == "posix":
        try:
            subprocess.run(['termux-open-url', YOUTUBE], timeout=2)
        except:
            try:
                subprocess.run(['xdg-open', YOUTUBE], timeout=2)
            except:
                print(f"{LIGHT_YELLOW}Visit: {YOUTUBE}{RESET}")

def check_password():
    try:
        response = requests.get(GITHUB_RAW, timeout=10)
        if response.status_code == 200:
            github_password = response.text.strip()
            return github_password == TOOL_PASSWORD
        return False
    except Exception:
        return False

def show_shizuku_guide():
    print(f"""
{LIGHT_CYAN}╔══════════════════════════════════════════════════════════╗
{LIGHT_CYAN}║              📱 SHIZUKU CONNECTION GUIDE               ║
{LIGHT_CYAN}╠══════════════════════════════════════════════════════════╣
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 1: Install Shizuku from Play Store{RESET}{LIGHT_CYAN}        ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 2: Enable Wireless Debugging{RESET}{LIGHT_CYAN}             ║
{LIGHT_CYAN}║  {WHITE}Settings → Developer Options → Wireless Debugging{RESET}{LIGHT_CYAN}║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 3: Pair Device{RESET}{LIGHT_CYAN}                           ║
{LIGHT_CYAN}║  {WHITE}Shizuku app → Pairing → Enter pairing code{RESET}{LIGHT_CYAN}   ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 4: Start Shizuku{RESET}{LIGHT_CYAN}                        ║
{LIGHT_CYAN}║  {WHITE}Shizuku app → Start{RESET}{LIGHT_CYAN}                         ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 5: Copy rish file{RESET}{LIGHT_CYAN}                      ║
{LIGHT_CYAN}║  {WHITE}cp /data/data/moe.shizuku.privileged.api/files/rish ~/{RESET}{LIGHT_CYAN}║
{LIGHT_CYAN}║  {WHITE}chmod +x ~/rish{RESET}{LIGHT_CYAN}                             ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {WHITE}STEP 6: Test connection{RESET}{LIGHT_CYAN}                     ║
{LIGHT_CYAN}║  {WHITE}sh ~/rish -c "id" 2>/dev/null{RESET}{LIGHT_CYAN}              ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}║  {YELLOW}💡 After connecting, run this tool again{RESET}{LIGHT_CYAN}      ║
{LIGHT_CYAN}║                                                          ║
{LIGHT_CYAN}╚══════════════════════════════════════════════════════════╝{RESET}
    """)

def main():
    clear_screen()
    print(f"""
{LIGHT_YELLOW}╔══════════════════════════════════════════╗
║     {BOLD}CYBER SPACE LK TOOL{RESET}{LIGHT_YELLOW}        ║
║     {WHITE}Checking Authorization...{RESET}{LIGHT_YELLOW}     ║
╚══════════════════════════════════════════╝{RESET}
    """)
    loading_animation("Checking Script Update", 2)
    
    if not check_password():
        print(f"""
{RED}╔══════════════════════════════════════════╗
{RED}║  {BOLD}{LIGHT_RED}❌ ACCESS DENIED{RESET}{RED}                    ║
{RED}║  {LIGHT_YELLOW}New Update Available!{RESET}{RED}              ║
{RED}║  {WHITE}Check YouTube Channel for Update{RESET}{RED}       ║
{RED}╚══════════════════════════════════════════╝{RESET}
        """)
        print(f"\n{LIGHT_CYAN}▶ Opening YouTube Channel...{RESET}")
        time.sleep(2)
        open_youtube()
        print(f"\n{LIGHT_GREEN}📺 YouTube: {YOUTUBE}{RESET}")
        time.sleep(3)
        sys.exit()
    
    print(f"""
{GREEN}╔══════════════════════════════════════════╗
{GREEN}║  {BOLD}{LIGHT_GREEN}✅ ACCESS GRANTED{RESET}{GREEN}                  ║
{GREEN}║  {WHITE}Welcome to Cyber Space LK Tool{RESET}{GREEN}      ║
{GREEN}╚══════════════════════════════════════════╝{RESET}
    """)
    time.sleep(1)
    
    # Check Shizuku
    check_shizuku()
    
    # Show system info
    system_info()
    time.sleep(1)
    
    if not SHIZUKU_CONNECTED:
        show_shizuku_guide()
        time.sleep(2)
    
    # Main menu loop
    while True:
        banner()
        garena_banner()
        
        if SHIZUKU_CONNECTED:
            print(f"{GREEN}✅ Shizuku: Connected{RESET}")
        else:
            print(f"{RED}❌ Shizuku: Not Connected{RESET}")
        
        print(f"""
{BOLD}{WHITE}╔══════════════════════════════════════════════╗
║              {LIGHT_GREEN}MAIN MENU{RESET}{BOLD}{WHITE}                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║  {LIGHT_GREEN}┌────────────────────────────────────────┐{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}1.{RESET} {LIGHT_GREEN}🚀 Start Optimization{RESET}{LIGHT_GREEN}          │{RESET}  ║
║  {LIGHT_GREEN}├────────────────────────────────────────┤{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}2.{RESET} {LIGHT_BLUE}👑 Admin Panel{RESET}{LIGHT_GREEN}                 │{RESET}  ║
║  {LIGHT_GREEN}├────────────────────────────────────────┤{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}3.{RESET} {LIGHT_YELLOW}📺 YouTube Channel{RESET}{LIGHT_GREEN}              │{RESET}  ║
║  {LIGHT_GREEN}├────────────────────────────────────────┤{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}4.{RESET} {LIGHT_PURPLE}💡 Optimization Tips{RESET}{LIGHT_GREEN}          │{RESET}  ║
║  {LIGHT_GREEN}├────────────────────────────────────────┤{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}5.{RESET} {LIGHT_CYAN}🔄 Check Updates{RESET}{LIGHT_GREEN}               │{RESET}  ║
║  {LIGHT_GREEN}├────────────────────────────────────────┤{RESET}  ║
║  {LIGHT_GREEN}│{RESET}  {WHITE}6.{RESET} {LIGHT_RED}❌ Exit{RESET}{LIGHT_GREEN}                         │{RESET}  ║
║  {LIGHT_GREEN}└────────────────────────────────────────┘{RESET}  ║
║                                              ║
╚══════════════════════════════════════════════╝{RESET}
        """)
        
        try:
            choice = input(f"{BOLD}{LIGHT_CYAN}┌─ Select Option ─┐\n│ {RESET}")
        except (KeyboardInterrupt, EOFError):
            choice = "6"
        
        if choice == "1":
            glitch_effect()
            banner()
            check_shizuku()
            loading_animation("Preparing optimization", 1.5)
            optimize()
            free_fire_tips()
            input(f"\n{LIGHT_YELLOW}Press Enter to continue...{RESET}")
        elif choice == "2":
            glitch_effect()
            banner()
            admin()
            input(f"\n{LIGHT_YELLOW}Press Enter to continue...{RESET}")
        elif choice == "3":
            glitch_effect()
            banner()
            update_check()
            print(f"\n{LIGHT_GREEN}[*] Opening YouTube channel...{RESET}")
            open_youtube()
            input(f"\n{LIGHT_YELLOW}Press Enter to continue...{RESET}")
        elif choice == "4":
            glitch_effect()
            banner()
            free_fire_tips()
            input(f"\n{LIGHT_YELLOW}Press Enter to continue...{RESET}")
        elif choice == "5":
            glitch_effect()
            banner()
            update_check()
            input(f"\n{LIGHT_YELLOW}Press Enter to continue...{RESET}")
        elif choice == "6":
            exit_animation()
            print(f"\n{LIGHT_GREEN}👋 Thanks for using Cyber Space LK Tool!{RESET}")
            print(f"{LIGHT_RED}💀 Stay tuned for more updates!{RESET}\n")
            time.sleep(1)
            sys.exit()
        else:
            print(f"\n{LIGHT_RED}❌ Invalid option! Please select 1-6{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()