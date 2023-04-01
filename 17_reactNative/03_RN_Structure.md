[TOC]

## Structure

```js
div -> View
p -> Text (all text `must be` inside the Text)
```

```js
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function App() {
  return (
    <View>
      {/* // # Prac1 */}
      <View style={styles.container}>
        <Text
          style={{
            fontSize: 28,
            color: "red",
          }}
        >
          Hello!
        </Text>
        {/* 시계, 배터리 등 상단 /style-auto../ */}
        <StatusBar style="dark" />
      </View>
      {/* // # Prac2 // View is a flex container and by default is column */}
      <View style={{ flex: 1 }}>
        <View style={{ flex: 1, backgroundColor: "green" }}></View>
        <View style={{ flex: 2, backgroundColor: "yellow" }}></View>
        <View style={{ flex: 1, backgroundColor: "orange" }}></View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
```
