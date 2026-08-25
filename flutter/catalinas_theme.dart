// Catalinas Design System — generated Flutter theme (do not edit)
import 'package:flutter/material.dart';

class CatColors {
  static const accent_active = Color(0xFF3d7ce0);
  static const accent_base = Color(0xFF5e9eff);
  static const accent_hover = Color(0xFF4a8df2);
  static const accent_on = Color(0xFFffffff);
  static const accent_ring = Color.fromARGB(40, 94, 158, 255);
  static const accent_subtle_a = Color.fromARGB(56, 94, 158, 255);
  static const accent_subtle_b = Color.fromARGB(30, 94, 158, 255);
  static const danger_base = Color(0xFFe8382d);
  static const danger_hover = Color(0xFFc22b21);
  static const danger_soft = Color(0xFFef5a76);
  static const dark_player_bg = Color.fromARGB(188, 24, 28, 42);
  static const dark_player_ink = Color(0xFFeef0f7);
  static const dark_player_ink_dim = Color.fromARGB(114, 238, 240, 247);
  static const doc_blue = Color(0xFF5f8af5);
  static const ink_faint = Color(0xFFaab1c2);
  static const ink_hi = Color(0xFF1c2436);
  static const ink_low = Color(0xFF8d95a8);
  static const ink_mid = Color(0xFF59627a);
  static const pink = Color(0xFFf2a2c6);
  static const ppt = Color(0xFFe8776f);
  static const stroke_dark = Color.fromARGB(20, 20, 30, 60);
  static const stroke_input = Color.fromARGB(35, 20, 30, 60);
  static const stroke_light = Color.fromARGB(140, 255, 255, 255);
  static const stroke_menu = Color.fromARGB(22, 0, 0, 0);
  static const stroke_softer = Color.fromARGB(12, 20, 30, 60);
  static const success = Color(0xFF34c759);
  static const surface_active = Color.fromARGB(22, 0, 0, 0);
  static const surface_card = Color.fromARGB(183, 255, 255, 255);
  static const surface_content = Color.fromARGB(221, 255, 255, 255);
  static const surface_glass_chip = Color.fromARGB(114, 255, 255, 255);
  static const surface_glass_window = Color.fromARGB(173, 247, 249, 253);
  static const surface_hover = Color.fromARGB(12, 0, 0, 0);
  static const surface_menu = Color.fromARGB(224, 246, 246, 250);
  static const surface_selected_on_accent = Color.fromARGB(239, 255, 255, 255);
  static const violet = Color(0xFFa78bfa);
  static const wallpaper_fallback_1 = Color(0xFFdbe7ff);
  static const wallpaper_fallback_2 = Color(0xFFffe3f0);
  static const wallpaper_fallback_3 = Color(0xFFded4ff);
  static const wallpaper_fallback_4 = Color(0xFFd3ecf5);
  static const warning = Color(0xFFff9f0a);
  static const white = Color(0xFFffffff);
}

class CatRadius {
  static double xs = 4.0;
  static double sm = 6.0;
  static double md = 8.0;
  static double lg = 12.0;
  static double xl = 16.0;
  static double window = 12.0;
  static double menu_item = 4.0;
  static double pill = 100.0;
}

class CatText {
  static TextTheme apply(BuildContext c) => Theme.of(c).textTheme.copyWith(
    bodyMedium: TextStyle(fontSize: 13, fontFamily: 'SF Pro Text', color: CatColors.ink_hi),
    labelSmall: TextStyle(fontSize: 11, letterSpacing: .4, color: CatColors.ink_low),
    titleLarge: TextStyle(fontSize: 17, fontWeight: FontWeight.w600, color: CatColors.ink_hi),
  );
}

ThemeData catLightTheme() => ThemeData(
  useMaterial3: true,
  scaffoldBackgroundColor: const Color(0xFFF2F4FA),
  colorScheme: ColorScheme.light(primary: Color(0xFF5e9eff), secondary: Color(0xFFa78bfa), error: Color(0xFFe8382d)),
  fontFamily: 'SF Pro Text',
);
