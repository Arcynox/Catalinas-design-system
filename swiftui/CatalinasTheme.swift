// Catalinas Design System - SwiftUI theme (generated)

import SwiftUI

public extension Color {
    init(catalinaHex hex: String) {
        let h = hex.replacingOccurrences(of: "#", with: "")
        var rgb: UInt64 = 0
        Scanner(string: h).scanHexInt64(&rgb)
        self.init(.sRGB,
                  red: Double((rgb >> 16) & 0xFF) / 255,
                  green: Double((rgb >> 8) & 0xFF) / 255,
                  blue: Double(rgb & 0xFF) / 255,
                  opacity: 1)
    }
}

public enum CatColors {
    public static let ColorAccentActive = Color(catalinaHex: "#3d7ce0")
    public static let ColorAccentBase = Color(catalinaHex: "#5e9eff")
    public static let ColorAccentHover = Color(catalinaHex: "#4a8df2")
    public static let ColorAccentOn = Color(catalinaHex: "#ffffff")
    public static let ColorDangerBase = Color(catalinaHex: "#e8382d")
    public static let ColorDangerHover = Color(catalinaHex: "#c22b21")
    public static let ColorDangerSoft = Color(catalinaHex: "#ef5a76")
    public static let ColorDarkPlayerInk = Color(catalinaHex: "#eef0f7")
    public static let ColorDocBlue = Color(catalinaHex: "#5f8af5")
    public static let ColorInkFaint = Color(catalinaHex: "#aab1c2")
    public static let ColorInkHi = Color(catalinaHex: "#1c2436")
    public static let ColorInkLow = Color(catalinaHex: "#8d95a8")
    public static let ColorInkMid = Color(catalinaHex: "#59627a")
    public static let ColorPink = Color(catalinaHex: "#f2a2c6")
    public static let ColorPpt = Color(catalinaHex: "#e8776f")
    public static let ColorSuccess = Color(catalinaHex: "#34c759")
    public static let ColorViolet = Color(catalinaHex: "#a78bfa")
    public static let ColorWallpaperFallback1 = Color(catalinaHex: "#dbe7ff")
    public static let ColorWallpaperFallback2 = Color(catalinaHex: "#ffe3f0")
    public static let ColorWallpaperFallback3 = Color(catalinaHex: "#ded4ff")
    public static let ColorWallpaperFallback4 = Color(catalinaHex: "#d3ecf5")
    public static let ColorWarning = Color(catalinaHex: "#ff9f0a")
    public static let ColorWhite = Color(catalinaHex: "#ffffff")
}

public enum CatRadius {
    public static let lg = CGFloat(12.0)
    public static let md = CGFloat(8.0)
    public static let menu_item = CGFloat(4.0)
    public static let pill = CGFloat(999.0)
    public static let sm = CGFloat(6.0)
    public static let window = CGFloat(12.0)
    public static let xl = CGFloat(16.0)
    public static let xs = CGFloat(4.0)
}

public extension Font {
    static let catBody = Font.system(size: 13, weight: .regular)
    static let catCaption = Font.system(size: 11, weight: .medium)
    static let catTitle = Font.system(size: 17, weight: .semibold)
}
